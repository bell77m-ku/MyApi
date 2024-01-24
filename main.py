from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
from functools import wraps

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME']='username'
app.config['BASIC_AUTH_PASSWORD']='12345678'

students = [{"name": "bunyarit", "id":"6530300317", "major": "T12"}]

@app.route('/')
def welcome():
    return "<h1>Welcome to Student Management API</h1>"

@app.route('/students', methods=["GET"])
def get_students():
    return jsonify({"students": students})


def run(host="localhost", port=80):
    app.run(host=host, port=port, debug=True)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
