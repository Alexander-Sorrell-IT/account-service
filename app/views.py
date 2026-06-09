from flask import Blueprint, jsonify

from .db import get_all_users

admin = Blueprint("admin", __name__)


@admin.route("/admin/users")
def list_users():
    """List every user in the system. Admin-only."""
    return jsonify(get_all_users())
