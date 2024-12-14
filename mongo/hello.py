from flask import Flask

app = Flask(__name__)

count_num = 0

@app.route("/")
def index():
    return "Thanks!"

@app.route("/hello")
def hello_world():
    return "Hello, world"

@app.route("/count")
def count():
    global count_num
    count_num += 1
    return f"Count is {count_num}"

@app.route("/json")
def json():
    my_json = {
        "id": "2",
        "name": "Matt",
        "type": "human",
        "color": "red",
        "age": 1,
        "valid": True
    }
    return my_json
