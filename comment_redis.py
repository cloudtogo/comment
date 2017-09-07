#!/usr/bin/python
# email: hongxi@cloudtogo.cn 2017.09.06 22：41
# update 2017-09-07 23:45
from flask import Flask, jsonify, make_response, request
from redis import Redis
import os

r = Redis(host = os.environ['REDIS_HOST'], port = 6379)

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def get_comments_raw (item_id):
    comments = r.get(item_id)
    if comments == None:
        comments = []
    else:
        comments = eval(comments)
    return comments

@app.route('/comment/<string:item_id>', methods=['GET'])
def get_comments(item_id):
    item_comments = get_comments_raw(item_id)
    return jsonify({'comments': item_comments})

@app.route('/comment/<string:item_id>', methods=['PUT'])
def add_comment(item_id):
    new_comment = {'user': request.json['user'], 'comment': request.json['comment']}
    item_comments = get_comments_raw(item_id)
    item_comments.append(new_comment)
    r.set(item_id, item_comments)
    return make_response(jsonify({'error': ''}), 200)
  

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
