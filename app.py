from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
#client = MongoClient('localhost', 27017)

@app.route('/')
def hello():
    return 'Hello World'        

if __name__ == "__main__":
    app.run(host="localhost", debug=True)