import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import seaborn as sns  # Corrected import name for seaborn

# Database connection details
db = 'D:\\PROGRAMMING\\Python Programming\\Devtown\\Projects\\Project 001\\movie.sqlite'
conn = sqlite3.connect(db)  # Establish a connection to the SQLite database
cur = conn.cursor()  # Create a cursor object to interact with the database

# 1. Top 10 highest budget movies
# Explanation:
# - Query the top 10 movies based on budget in descending order.
cur.execute("SELECT * FROM movies ORDER BY budget DESC LIMIT 10")
top_budget_movies = cur.fetchall()
top_budget_movies_df = pd.DataFrame(
    top_budget_movies,
    columns=[
        'id', 'original_title', 'budget', 'popularity', 'release_date', 'revenue',
        'title', 'vote_average', 'vote_count', 'overview', 'tagline', 'uid', 'director_id'
    ]
)
print("Top 10 highest budget movies:")
print(top_budget_movies_df)

# 2. Top 10 revenue-making movies
# Explanation:
# - Query the top 10 movies based on revenue in descending order.
cur.execute("SELECT * FROM movies ORDER BY revenue DESC LIMIT 10")
top_revenue_movies = cur.fetchall()
top_revenue_movies_df = pd.DataFrame(
    top_revenue_movies,
    columns=[
        'id', 'original_title', 'budget', 'popularity', 'release_date', 'revenue',
        'title', 'vote_average', 'vote_count', 'overview', 'tagline', 'uid', 'director_id'
    ]
)
print("Top 10 revenue-making movies:")
print(top_revenue_movies_df)

# 3. Most popular movies with the highest vote average
# Explanation:
# - Query the top 10 movies based on vote average in descending order.
cur.execute("SELECT * FROM movies ORDER BY vote_average DESC LIMIT 10")
highest_voted_movies = cur.fetchall()
highest_voted_movies_df = pd.DataFrame(
    highest_voted_movies,
    columns=[
        'id', 'original_title', 'budget', 'popularity', 'release_date', 'revenue',
        'title', 'vote_average', 'vote_count', 'overview', 'tagline', 'uid', 'director_id'
    ]
)
print("Top 10 most popular movies with the highest vote average:")
print(highest_voted_movies_df)

# 4. Directors with the number of movies and total revenue
# Explanation:
# - Join `movies` and `directors` tables.
# - Group by director name to calculate the total number of movies and sum of revenues.
cur.execute("""
    SELECT name, COUNT(*), SUM(revenue) 
    FROM directors 
    JOIN movies ON movies.director_id = directors.id 
    GROUP BY name 
    ORDER BY SUM(revenue) DESC
""")
directors_revenue = cur.fetchall()
directors_revenue_df = pd.DataFrame(
    directors_revenue,
    columns=['Name', 'Total Movies', 'Total Revenue']
)
print("Top directors by revenue:")
print(directors_revenue_df.head(10))

# 5. Directors with the highest number of movies and revenue
# Explanation:
# - Same as above but ordered by the number of movies instead of revenue.
cur.execute("""
    SELECT name, COUNT(*), SUM(revenue) 
    FROM directors 
    JOIN movies ON movies.director_id = directors.id 
    GROUP BY name 
    ORDER BY COUNT(original_title) DESC
""")
directors_movie_count = cur.fetchall()
directors_movie_count_df = pd.DataFrame(
    directors_movie_count,
    columns=['Name', 'Total Movies', 'Total Revenue']
)
print("Top directors by the number of movies:")
print(directors_movie_count_df.head(10))

# 6. Movies directed by Steven Spielberg
# Explanation:
# - Fetch movie details for movies directed by Steven Spielberg.
# - Ordered by vote average in descending order for better insight into his best-rated movies.
cur.execute("""
    SELECT original_title, release_date, budget, revenue, popularity, vote_average 
    FROM movies 
    JOIN directors ON directors.id = movies.director_id 
    WHERE name = "Steven Spielberg" 
    ORDER BY vote_average DESC
""")
movies_by_steven_spielberg = cur.fetchall()
movies_by_steven_spielberg_df = pd.DataFrame(
    movies_by_steven_spielberg,
    columns=['Original Title', 'Release Date', 'Budget', 'Revenue', 'Popularity', 'Vote Average']
)
print("Movies directed by Steven Spielberg:")
print(movies_by_steven_spielberg_df)

# Close the database connection to release resources
conn.close()
