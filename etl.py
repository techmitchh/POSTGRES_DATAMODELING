import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    - Itterates through song_data in Json files
    
    - Extracts data for song and artist table and inserts into Dataframe
    
    - Transform Dataframe and inserts data into table

    """
    # open song file
    df = pd.read_json(filepath, lines = True)
    
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
    """
    - Itterates through log_data in Json files
    
    - Extracts data for log and inserts into Dataframe
    
    - Transforms 'ts' timstamp column by splitting data into seperate columns
      and inserts data into time table

    - Clean and transform data into dataframe then insert into user_table
    
    - songplay_data: Retrieves the matching song_id and artist_id

    - Inserts data into songplay_table 

    """
    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[df.page.isin(['NextSong'])] 

    # convert timestamp column to datetime
    df['ts'] = pd.to_datetime(df['ts'], unit='ms') # changes timstamp from ms to datetime timestamp
    
    # insert time data records
    df['start_time'] = df['ts'].dt.strftime('%H:%M:%S.%f')

    # Splits data in timestamp column into multiple columns
    start_time = df['start_time']
    hour = df['ts'].dt.hour
    day = df['ts'].dt.day  
    weekofyear = df['ts'].dt.strftime('%W')
    month = df['ts'].dt.month
    year = df['ts'].dt.year
    weekday = df['ts'].dt.dayofweek # The day of the week with Monday=0, Sunday=6.

    # Create a list out of the seperate timestamp columns
    time_data = [start_time, hour, day, weekofyear, month, year, weekday]

    # Create Column Names and Combines time_data with columns to create a Dataframe
    column_labels = ('start_time','hour','day','weekofyear','month','year','weekday')
    column_data = {column_labels[0]: pd.Series(time_data[0]),
                column_labels[1]: pd.Series(time_data[1]),
                column_labels[2]: pd.Series(time_data[2]),
                column_labels[3]: pd.Series(time_data[3]),
                column_labels[4]: pd.Series(time_data[4]),
                column_labels[5]: pd.Series(time_data[5]),
                column_labels[6]: pd.Series(time_data[6])}
    
    time_df = pd.DataFrame(column_data)

    # iterrates through each row of data and inserts it into time_table
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    df['userAgent'] = df['userAgent'].str.strip('""')
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (row.start_time, str(row.userId), row.level, song_id, artist_id, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    - Iterrates through all files and sends the filepath document to
      either process_song_file or process_log_file

    - Files are enumerated while data is being processed
    
    """
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