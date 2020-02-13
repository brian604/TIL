from flask import Flask, render_template
from flask.json import jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('memo.html')


@app.route('/bookmark', methods=['POST'])
def bookmark_post():
    doc = {
        'title' : "1",
        "image" : "2" ,
        "desc" : "3",
        "url" : "4"
    }
    #db.bookmarks_test.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/bookmark', methods=['GET'])
def bookmark_get():
    bookmarks = list(db.movies.find_one({}))
    print(bookmarks)
    return jsonify(bookmarks)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
