# File: app/routes/auth.py

from flask import Blueprint, request, jsonify
from app.utils.jwt_helper import create_token, verify_token, JWTError
from app.models.user import User

auth = Blueprint("auth", __name__)

# Fake login route
@auth.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")  # not validated yet

    user = User.find_by_username(username)
    if not user:
        return jsonify({"error": "Invalid username"}), 401

    # create JWT
    token = create_token({"sub": user.user_id, "username": user.username, "role": user.role})
    return jsonify({"token": token})


# Protected route
@auth.route("/protected", methods=["GET"])
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Missing token"}), 401

    try:
        decoded = verify_token(token.split(" ")[1])  # expects "Bearer <token>"
        return jsonify({"message": "Access granted", "user": decoded})
    except JWTError as e:
        return jsonify({"error": str(e)}), 401
