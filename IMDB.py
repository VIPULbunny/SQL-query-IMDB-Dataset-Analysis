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

# 8. Find the name of the 10th first woman director
# Explanation:
# - Query all female directors and fetch the 10th one (index 9 in zero-based indexing).
cur.execute("SELECT Name FROM directors WHERE Gender == '1'")
female_directors = cur.fetchall()
if len(female_directors) >= 10:
    print("The 10th woman director is:", female_directors[9][0])
else:
    print("There are less than 10 female directors in the database.")

# 9. What are the three most popular movies
# Explanation:
# - Order the movies by their popularity in descending order and fetch the top 3.
cur.execute("SELECT Title FROM movies ORDER BY Popularity DESC LIMIT 3")
top_popular_movies = cur.fetchall()
print("The three most popular movies are:")
for i, movie in enumerate(top_popular_movies, start=1):
    print(f"{i}. {movie[0]}")

# 10. What are the three most bankable movies
# Explanation:
# - Order the movies by their budget in descending order and fetch the top 3.
cur.execute("SELECT Title FROM movies ORDER BY Budget DESC LIMIT 3")
top_bankable_movies = cur.fetchall()
print("The three most bankable movies are:")
for i, movie in enumerate(top_bankable_movies, start=1):
    print(f"{i}. {movie[0]}")

# 11. What is the most awarded and average voted movie since Jan 1st, 2000
# Explanation:
# - Filter movies released after '2000-01-01' and order by vote average in descending order.
cur.execute("SELECT Original_Title FROM movies WHERE Release_Date > '2000-01-01' ORDER BY Avg_Ratings DESC LIMIT 1")
most_awarded_movie = cur.fetchall()
if most_awarded_movie:
    print("The most awarded and average voted movie since Jan 1st, 2000 is:", most_awarded_movie[0][0])
else:
    print("No movies found meeting the criteria.")

# 12. Which movies were directed by Brenda Chapman?
# Explanation:
# - Perform a JOIN between the `movies` and `directors` tables to find movies directed by 'Brenda Chapman'.
cur.execute("""
    SELECT Original_Title 
    FROM movies 
    JOIN directors ON directors.ID = movies.Director_id 
    WHERE directors.Name = 'Brenda Chapman'
""")
brenda_chapman_movies = cur.fetchall()
if brenda_chapman_movies:
    print("Movies directed by Brenda Chapman:")
    for movie in brenda_chapman_movies:
        print(f"- {movie[0]}")
else:
    print("No movies directed by Brenda Chapman found in the database.")

# Close the database connection to release resources
conn.close()

