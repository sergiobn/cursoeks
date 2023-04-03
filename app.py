import os
from flask import Flask, jsonify, request
from Models.posts import posts
app = Flask(__name__)


@app.route("/")
def main():
    return jsonify({"status": "Welcome!"})


@app.route('/posts', methods=['GET'])
def hello():
    return jsonify({"posts": posts})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)