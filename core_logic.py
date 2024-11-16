users = {}


def create_user(user_id: int, name: str, username: str, email: str):
    if user_id in users:
        raise ValueError("User already exists")
    users[user_id] = {"id": user_id, "name": name, "username": username, "email": email}
    return users[user_id]


def get_user(user_id: int):
    if user_id not in users:
        raise ValueError("User not found")
    return users[user_id]
