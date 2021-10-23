# Project: Data Modeling with Python and Postgres

***

### Overview

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

You will not be able to run test.ipynb, etl.ipynb, or etl.py until you have run create_tables.py at least once to create the sparkifydb database, which these other files connect to.

***

### Dependencies

##### Use the following Python libraries:

- os
- glob
- psycopg2
- pandas as pd
- from sql_queries import *

## Entity Relationship Diagram

![SparkifyERD](/images/SparkifyERD.png "Sparkify ERD")
