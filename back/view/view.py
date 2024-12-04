from flask import Blueprint, request, jsonify
from controller.controller import UserController

app_route = Blueprint("user", __name__)


@app_route.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()

    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"message": f"{field.capitalize()} is required!"}), 400

    response, error = UserController.create_user(data)
    if error:
        return jsonify({"message": error}), 409 if "exists" in error else 500

    return jsonify(response), 201


@app_route.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()

    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"message": f"{field.capitalize()} is required!"}), 400

    response, error = UserController.login_user(data)

    if error:
        return jsonify({"message": error}), 404
    return jsonify(response), 200


@app_route.route("/read/<uuid>", methods=["GET"])
def read_user(uuid):
    response, error = UserController.get_user(uuid)
    if error:
        return jsonify({"message": error}), 404
    return jsonify(response), 200


@app_route.route("/update/<uuid>", methods=["PUT"])
def update_user(uuid):
    data = request.get_json()

    required_fields = ["email", "password"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"message": f"{field.capitalize()} is required!"}), 400

    response, error = UserController.update_user(uuid, data)
    if error:
        return jsonify({"message": error}), 404

    return jsonify(response), 200


@app_route.route("/delete/<uuid>", methods=["DELETE"])
def delete_user(uuid):
    response, error = UserController.delete_user(uuid)
    if error:
        return jsonify({"message": error}), 404

    return jsonify(response), 200
