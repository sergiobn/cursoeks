import os
from flask import Flask, jsonify, request
from Models.posts import posts,Post
app = Flask(__name__)


@app.route("/")
def main():
    return jsonify({"status": "Welcome!"})


@app.route('/posts', methods=['GET'])
def hello():
    return jsonify({"posts": posts})

@app.route('/post', methods=['POST', 'GET'])
def add_post():
    post = Post(request.json["title"], request.json["description"])
    posts.append(post)
    return jsonify(post.to_json()), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)