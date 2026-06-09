_USERS = [
    {"id": 1, "name": "ada", "role": "admin"},
    {"id": 2, "name": "grace", "role": "user"},
]


def get_all_users():
    """Return every user record (includes roles — admin-only data)."""
    return _USERS
