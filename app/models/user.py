# File: app/models/user.py

class User:
    """Temporary User model for testing JWT auth system."""

    def __init__(self, user_id: str, username: str, role: str):
        self.user_id = user_id
        self.username = username
        self.role = role

    # fake function to mimic DB lookup
    @staticmethod
    def find_by_username(username: str):
        # for now, return a hardcoded user (later integrate DB)
        if username == "admin":
            return User("1", "admin", "admin")
        elif username == "student":
            return User("2", "student", "student")
        return None
