from flask import Blueprint, request, jsonify

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/api/login", methods=["POST"])
def login():
    data = request.json
    # Dummy logic
    return jsonify({"message": f"Logged in as {data.get('username')}"})
