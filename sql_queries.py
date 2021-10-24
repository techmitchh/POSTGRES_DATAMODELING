# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table;"
user_table_drop = "DROP TABLE IF EXISTS user_table;"
song_table_drop = "DROP TABLE IF EXISTS song_table;"
artist_table_drop = "DROP TABLE IF EXISTS artist_table;"
time_table_drop = "DROP TABLE IF EXISTS time_table;"

# CREATE TABLES

# FACT TABLE
songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id serial PRIMARY KEY,
                                start_time TIMESTAMP NOT NULL, 
                                userId INT NOT NULL, 
                                level VARCHAR, 
                                song_id VARCHAR, 
                                artist_id VARCHAR, 
                                session_id INT, 
                                location VARCHAR, 
                                userAgent VARCHAR
                                );
""")

# DIM TABLES
user_table_create = (""" CREATE TABLE IF NOT EXISTS users (
                            userId INT PRIMARY KEY, 
                            firstName VARCHAR NOT NULL, 
                            lastName VARCHAR NOT NULL, 
                            gender VARCHAR, 
                            level VARCHAR
                            );
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (
                            song_id VARCHAR PRIMARY KEY, 
                            title VARCHAR NOT NULL, 
                            artist_id VARCHAR NOT NULL, 
                            year INT, 
                            duration FLOAT
                            );
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
                              artist_id VARCHAR PRIMARY KEY, 
                              artist_name VARCHAR NOT NULL, 
                              artist_location VARCHAR, 
                              artist_latitude FLOAT, 
                              artist_longitude FLOAT
                              );
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (
                            start_time TIMESTAMP PRIMARY KEY, 
                            hour INT NOT NULL, 
                            day INT NOT NULL, 
                            weekofyear INT NOT NULL, 
                            month INT NOT NULL, 
                            year INT NOT NULL, 
                            weekday INT NOT NULL
                            );
""")

# INSERT RECORDS
songplay_table_insert = (""" INSERT INTO songplays (start_time, userId, level, song_id, artist_id, session_id, location, userAgent)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

user_table_insert = (""" INSERT INTO users (userId, firstName, lastName, gender, level)
                         VALUES (%s, %s, %s, %s, %s) 
                         ON CONFLICT (userId)
                         DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration)
                         VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                           VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, weekofyear, month, year, weekday)
                         VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = (""" select songs.song_id, artists.artist_id
                     from songs
                     join artists
                       on songs.artist_id = artists.artist_id
                      and songs.title = %s
                    where artists.artist_name = %s
                      and songs.duration = %s  
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]