from functools import wraps
from flask import request, jsonify
from models import User

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_id = request.headers.get("User-Id") or request.headers.get("user_id")

            if not user_id:
                return jsonify({"error": "Missing user ID"}), 401

            user = User.query.get(user_id)
            if not user or user.role != required_role:
                return jsonify({"error": "Forbidden: Insufficient role"}), 403

            return f(*args, **kwargs)
        return wrapped
    return decorator
