import pandas as pd
from pymongo import MongoClient

df = pd.read_csv('movies_data.csv')

print(df)

client = MongoClient('mongodb://localhost:27017/')

db = client['mydatabase']

collection = db['mycollection']

data = df.to_dict(orient='records')

collection.insert_many(data)
