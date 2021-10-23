# Project: Data Modeling with Python and PostgreSQL

***

### Overview

Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. A star schema has been implemented to provide simple queries to aggregate data quickly and effectively. The current ETL pipeline will allow the Sparkify team to add Json files to the existing folder and query that information quickly.

In this project, I'll apply what I've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, I will define the fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL. 

***

### Features

- Creates songplay fact table.
- Creates (user, song, artist, and time) dimension tables.
- Iterrates through multiple CSVs and **extracts** song and log data.
- **Transforms** and clean to prepare for table insertion.
- Implements a song_select query that finds and matches song_id and artist_id based on song title, artist name, and duration of song.
- **Inserts** data into respective Postgres database table.

***

### Running the project

Files in respository:

- **create_tables.py**: Establishes connection to sparkify db creates db, drops tables (if exits), creates tables
- **sql_queries**: Provides sql syntax to drop tables, create fact and dimension table, insert records, find songs, and query lists.
- **etl.ipynb**: Provides a testing environment to building ETL pipeline.
- **etl.py**: Production ready ETL pipeline. Runs necessary functions that Extracts, Transforms, and Loads data into Sparkify db. Code has been copied from etl.ipynb.
- **test.ipynb**: Runs queries to test data has been inserted into sparkify db.
- **log_data, song_data** folders: holds the data necessary for the Sparkify project.

You will not be able to run test.ipynb, etl.ipynb, or etl.py until you have run create_tables.py at least once to create the sparkifydb database, which these other files connect to.

***

### Dependencies

- postgresql database

##### Use the following Python libraries:

- os
- glob
- psycopg2
- pandas as pd
- from sql_queries import *

***

## Entity Relationship Diagram

![SparkifyERD](/images/SparkifyERD.png "Sparkify ERD")
