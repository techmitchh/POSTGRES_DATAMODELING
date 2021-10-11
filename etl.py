import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    # song_files = get_files('song_data')

    # filepath = 'e:\\Udacity\\UdacityProjects\\postgres_datamodeling\\song_data\\A\\A\\A\\TRAAAAW128F429D538.json'
    df = pd.read_json(filepath, lines = True)
    # df = pd.DataFrame()
    # for file in song_files:
    #     tmp_df = pd.read_json(file, lines=True)
    #     df = df.append(tmp_df)

    # insert song record
    s = df[['song_id','title','artist_id','year','duration']].copy()
    song_data = s.values.tolist()
    for song in song_data:
        cur.execute(song_table_insert, song)
    
    # insert artist record
    a = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].copy()
    artist_data = a.values.tolist()
    for artist in artist_data:
        cur.execute(artist_table_insert, artist)
    


def process_log_file(cur, filepath):
    # open log file
    # filepath = 'e:\\Udacity\\UdacityProjects\\postgres_datamodeling\\log_data\\2018\\11\\2018-11-01-events.json'
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[df.page.isin(['NextSong'])] 

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms') # changes timstamp from ms to datetime timestamp
    
    # insert time data records
    hour = df['ts'].dt.hour
    day = df['ts'].dt.dayofweek
    weekofyear = df['ts'].dt.weekofyear
    month = df['ts'].dt.month
    year = df['ts'].dt.year
    time_data = [hour,day,weekofyear,month,year]

    column_labels = ('hour','day','weekofyear','month','year')
    column_data = {column_labels[0]: pd.Series(time_data[0]),
                column_labels[1]: pd.Series(time_data[1]),
                column_labels[2]: pd.Series(time_data[2]),
                column_labels[3]: pd.Series(time_data[3]),
                column_labels[4]: pd.Series(time_data[4])}
    
    time_df = pd.DataFrame(column_data)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, str(row.userId), row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='song_data', func=process_song_file)
    process_data(cur, conn, filepath='log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()