# Code to create a README.md file for the project
readme_content = """
# Movie Analytics Using SQLite and Python

---

## Overview
This project focuses on analyzing movie data stored in an SQLite database using Python. It performs various analyses, including exploring top movies by budget, revenue, and vote averages, identifying prolific and bankable directors, and generating insights into movie trends.

---

## Features
1. **Database Connectivity**: 
   - Connects to an SQLite database (`movie.sqlite`) to fetch and analyze data.

2. **Key Analyses**:
   - **Budget Analysis**: Identifies the top 10 highest-budget movies.
   - **Revenue Analysis**: Lists the top 10 revenue-generating movies.
   - **Voting Analysis**: Determines the most popular movies based on vote averages.
   - **Director Insights**:
     - Top directors by total revenue and number of movies directed.
     - Most prolific and bankable directors.
   - **Specific Analysis**:
     - Fetches details of movies directed by Steven Spielberg.
     - Analyzes gender-based trends among directors.

3. **Visualization Tools**:
   - `Matplotlib` and `Seaborn` for plotting trends and relationships in data.

---

## Technologies Used
- **Python Libraries**:
  - `Pandas` and `NumPy` for data manipulation.
  - `Matplotlib` and `Seaborn` for visualizations.
  - `SQLite3` for database interaction.
- **SQL**:
  - Advanced queries for data extraction and aggregation.

---

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-analytics-using-sqlite.git
