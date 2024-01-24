from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME']='username'
app.config['BASIC_AUTH_PASSWORD']='12345678'
basic_auth=BasicAuth(app)

students = [{"name": "bunyarit", "std_id":6530300317, "major": "T12"}]


@app.route('/')
def welcome():
    return "<h1>Welcome to Student Management API</h1>"


@app.route('/students', methods=["GET"])
@basic_auth.required
def get_students():
    return jsonify({"students": students})

@app.route('/students/<int:std_id>', methods=["GET"])
@basic_auth.required
def get_student(std_id):
    student = next((s for s in students if s["std_id"]==std_id), None)
    if student:
        return jsonify({"students": students}), 200
    else:
        return jsonify({"error":"Student not found"}), 404


@app.route('/students', methods=["POST"])
@basic_auth.required
def post_students():
    data = request.get_json()
    std_id = next((s for s in students if s["std_id"] != data["std_id"]), None)
    if std_id:
        new_std = {
            "name": data["name"],
            "std_id": data["std_id"],
            "major": data["major"]
        }
        students.append(new_std)
        return jsonify(new_std), 200
    else:
        return jsonify({"error":"Cannot create new student"})

def run(host="127.0.0.1", port=80):
    app.run(host=host, port=port, debug=True)

if __name__ == '__main__':
    run()
