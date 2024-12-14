import pandas as pd
from sqlalchemy import create_engine, text

host = "localhost"
user = "root"
password = ""
database = "imdb_netflix_db"
connection_url = f"mysql+mysqlconnector://{user}:{password}@{host}:3306/{database}"
engine = create_engine(connection_url, echo=True)

imdb_movies = pd.read_csv("movies_data.csv")
netflix_titles = pd.read_csv("netflix_titles.csv")

with engine.connect() as connection:
    imdb_movies.to_sql("imdb_movies", connection, if_exists='replace', index=False)
    netflix_titles.to_sql("netflix_titles", connection, if_exists='replace', index=False)

with engine.connect() as connection:
    results = connection.execute(text("SELECT * FROM imdb_movies LIMIT 10"))
    for row in results.mappings():
        print(row)
    
    results = connection.execute(text("SELECT * FROM netflix_titles LIMIT 10"))
    for row in results.mappings():
        print(row)
    
    query = """
    SELECT imdb_movies.Series_Title, imdb_movies.IMDB_Rating, netflix_titles.type
    FROM imdb_movies
    JOIN netflix_titles ON imdb_movies.Series_Title = netflix_titles.title
    LIMIT 10
    """
    results = connection.execute(text(query))
    for row in results.mappings():
        print(row)