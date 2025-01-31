from flask import Flask, jsonify, render_template, request, send_from_directory
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS
import time

app = Flask(__name__, static_folder="static")

client = MongoClient("mongodb://localhost:27017/")

db = client["my_database"]
users_collection = db["users"]

CORS(app)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_static_files(path):
    if path == "" or path == "index.html":
        
        return send_from_directory(app.static_folder, "index.html")
    else:
      
        return send_from_directory(app.static_folder, path)


@app.route('/error')
def error():
    return render_template('error.html', message='MongoDB connection failed! Please check the database server.')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# CREATE
@app.route("/users/new", methods=["POST"])
def create_user():
    try:
        data = request.json

        
        data["created_ts"] = float(int(time.time()))

        users_collection.insert_one(data)

        return jsonify({"message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# GET ALL
@app.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find())

    for user in users:
        user["_id"] = str(user["_id"])

    return jsonify(users)

# GET
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    try:
        if not ObjectId(id):
            return jsonify({"error": "Invalid ID"}), 400
        data =  users_collection.find_one({"_id": ObjectId(id)})

        if not data:
            return jsonify({"msg": "User not found"}),404
        
        data["_id"] = str(data["_id"])

        return jsonify({"user":data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# UPDATE
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    try:
        if not ObjectId(id):
            return jsonify({"error": "Invalid ID"}), 400
        data = request.json

        if not data:
            return jsonify({"msg": "No data entered for update"}), 400
        
        data["updated_ts"] = float(int(time.time()))
        result = users_collection.update_one({"_id": ObjectId(id)}, {"$set": data})

        if result.matched_count == 0:
            return jsonify({"msg": "User not found"}), 404
        
        return jsonify({"msg": "User updated"}), 200
    except Exception as e:
        jsonify({"error": str(e)}), 500

# DELETE    
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        if not ObjectId(id):
            return jsonify({"msg":"Invalid ID"}), 400
        result = users_collection.delete_one({"_id": ObjectId(id)})

        if result.deleted_count == 0:
            return jsonify({"msg": "User not found"}), 404
        return jsonify({"msg": "User successfully deleted", "id": id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
          
if __name__ == "__main__":
    app.run(debug=True)
