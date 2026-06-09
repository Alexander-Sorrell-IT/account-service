from functools import wraps
from flask import request, jsonify

from .tokens import verify_token


def login_required(view):
    """Reject the request unless it carries a valid session token."""

    @wraps(view)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization", "")
        if not verify_token(token):
            return jsonify({"error": "unauthorized"}), 401
        return view(*args, **kwargs)

    return wrapper
