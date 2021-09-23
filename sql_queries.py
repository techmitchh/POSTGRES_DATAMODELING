# DROP TABLES

songplay_table_drop = ""
user_table_drop = ""
song_table_drop = "DROP TABLE IF EXISTS song_table;"
artist_table_drop = "DROP TABLE IF EXISTS artist_table;"
time_table_drop = ""

# CREATE TABLES

songplay_table_create = ("""
""")

user_table_create = ("""
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS song_table (song_id varchar, title varchar, artist_id varchar, year int, duration int);
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artist_table (artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude float, artist_longitude float);
""")

time_table_create = ("""
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = (""" INSERT into song_table (song_id, title, artist_id, year, duration)
                         VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = (""" INSERT into artist_table (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                            VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [song_table_create, artist_table_create]
drop_table_queries = [song_table_drop, artist_table_drop]
# create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
# drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]