from flask import Flask, jsonify, request
import requests
from requests.auth import HTTPBasicAuth


import os


app = Flask(__name__)

@app.route("/")
def root():
    return "Home"

@app.route("/users/<string:user_id>")
def get_user(user_id):
    user = {"id":user_id, "name": "test", "telefono": "97465121"}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route("/users", methods=['POST'])
def creare_users():
    data = request.get_json()
    return jsonify(data), 201

#@app.route("/")
#def root():
#
#    #return "Home"

if __name__=="__main__":
    app.run(debug=True)
