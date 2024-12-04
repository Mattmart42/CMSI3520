from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

@app.route('/data', methods=['GET'])
def get_all_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

@app.route('/data/<key>/<value>', methods=['GET'])
def filter_data(key, value):
    if value.lower() == 'nan':
        value = None

    query = {key: value}

    data = list(collection.find(query, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)