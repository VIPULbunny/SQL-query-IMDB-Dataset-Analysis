import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3  # Serverless database for lightweight database operations

# Database connection details
db = 'D:\\PROGRAMMING\\Python Programming\\Devtown\\Projects\\Project 001\\movie.sqlite'
conn = sqlite3.connect(db)  # Establish a connection to the SQLite database
cur = conn.cursor()  # Create a cursor object to interact with the database

# 1. Fetch all movies from the database
# Explanation:
# - Query the `movies` table to fetch all its records.
# - Create a DataFrame with appropriate column names for better data manipulation.
cur.execute("SELECT * FROM movies")
movies = cur.fetchall()
movies_df = pd.DataFrame(
    movies,
    columns=[
        'ID', 'Original_Title', 'Budget', 'Popularity', 'Release_Date', 'Revenue',
        'Title', 'Avg_Ratings', 'Rating_Count', 'Overview', 'Tagline', 'Uid', 'Director_id'
    ]
)
print("Movies DataFrame:")
print(movies_df.head())
print(movies_df.info())

# 2. Fetch all directors from the database
# Explanation:
# - Query the `directors` table to fetch all its records.
# - Create a DataFrame for better organization and analysis.
cur.execute("SELECT * FROM directors")
directors = cur.fetchall()
directors_df = pd.DataFrame(
    directors,
    columns=['Name', 'ID', 'Gender', 'Uid', 'Department']
)
print("Directors DataFrame:")
print(directors_df.head())

# 3. Count the total number of movies
# Explanation:
# - Use the `COUNT` SQL function to determine the total number of movies.
cur.execute("SELECT COUNT(Title) FROM movies")
movie_count = cur.fetchall()[0][0]
print("Total number of movies in the database:", movie_count)

# 4. Find specific directors: James Cameron, Luc Besson, John Woo
# Explanation:
# - Use an `IN` clause to filter for specific director names.
cur.execute("SELECT * FROM directors WHERE Name IN ('James Cameron', 'Luc Besson', 'John Woo')")
specific_directors = cur.fetchall()
specific_directors_df = pd.DataFrame(
    specific_directors,
    columns=['Name', 'ID', 'Gender', 'Uid', 'Department']
)
print("Specific Directors DataFrame:")
print(specific_directors_df)

# 5. Find all director names starting with 'Steven'
# Explanation:
# - Use the `LIKE` operator with a wildcard to filter names starting with 'Steven'.
cur.execute("SELECT * FROM directors WHERE Name LIKE 'Steven%'")
steven_directors = cur.fetchall()
steven_directors_df = pd.DataFrame(
    steven_directors,
    columns=['Name', 'ID', 'Gender', 'Uid', 'Department']
)
print("Directors whose names start with 'Steven':")
print(steven_directors_df)

# 6. Count the number of female directors
# Explanation:
# - Use the `COUNT` SQL function to count entries where `Gender` is '1', indicating female.
cur.execute("SELECT COUNT(*) FROM directors WHERE Gender == '1'")
female_director_count = cur.fetchall()[0][0]
print("Number of female directors in the IMDB database:", female_director_count)

# Close the database connection to release resources
conn.close()
