from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('db', 27017)
db = client.test

@app.route('/')
def hello():
    return 'Hello World v3'        

@app.route('/create_post',methods=['GET','POST'])
def create_post():
    post={"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"]
    }
    db.posts.insert(post)

    # return all posts
    posts=db.posts.count()
    return str(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)