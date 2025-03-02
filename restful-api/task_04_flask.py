#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API"

users = {}

@app.route("/data")
def get_name_user():
    user_name = list(users.keys())
    return jsonify(user_name)

@app.route("/status")
def stats():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user_information = users.get(username)
    if user_information is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_information)

@app.route("/add_user", methods=["POST"])
def post_user():
    create = request.get_json()
    new_user = create.get('username')
    new_name = create['name']
    new_age = create['age']
    new_city = create['city']

    if not isinstance(new_user, str) or new_user == "":
        return jsonify({"error": "Username is required"}), 400

    if new_user in users:
        return jsonify({"error": "Username already exists"}), 400

    users[new_user] = {"username": new_user, "name": new_name, "age": new_age, "city": new_city}

    message = {"message": "User added", "user": users[new_user]}
    return jsonify(message), 201

if __name__ == "__main__":
    app.run(debug=True)
