# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay_table;"
user_table_drop = "DROP TABLE IF EXISTS user_table;"
song_table_drop = "DROP TABLE IF EXISTS song_table;"
artist_table_drop = "DROP TABLE IF EXISTS artist_table;"
time_table_drop = "DROP TABLE IF EXISTS time_table;"

# CREATE TABLES

# FACT TABLE
songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplay_table (
                                songplay_id serial,
                                start_time time, 
                                userId int, 
                                level varchar, 
                                song_id varchar, 
                                artist_id varchar, 
                                session_id int, 
                                location varchar, 
                                userAgent varchar)
""")

# DIM TABLES
user_table_create = (""" CREATE TABLE IF NOT EXISTS user_table (
                            userId int, 
                            firstName varchar, 
                            lastName varchar, 
                            gender varchar, 
                            level varchar
                            );
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS song_table (
                            song_id varchar, 
                            title varchar, 
                            artist_id varchar, 
                            year int, 
                            duration float
                            );
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artist_table (
                              artist_id varchar, 
                              artist_name varchar, 
                              artist_location varchar, 
                              artist_latitude float, 
                              artist_longitude float
                              );
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time_table (
                            start_time time, 
                            hour int, 
                            day int, 
                            weekofyear int, 
                            month int, 
                            year int, 
                            weekday int
                            );
""")

# INSERT RECORDS
songplay_table_insert = (""" INSERT INTO songplay_table (start_time, userId, level, song_id, artist_id, session_id, location, userAgent)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = (""" INSERT into user_table (userId, firstName, lastName, gender, level)
                         VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = (""" INSERT into song_table (song_id, title, artist_id, year, duration)
                         VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = (""" INSERT into artist_table (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                           VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = (""" INSERT into time_table (start_time, hour, day, weekofyear, month, year, weekday)
                         VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = (""" select song_table.song_id, artist_table.artist_id
                     from song_table
                     join artist_table
                       on song_table.artist_id = artist_table.artist_id
                      and song_table.title = %s
                    where artist_table.artist_name = %s
                      and song_table.duration = %s  
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]