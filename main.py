from fastapi import FastAPI, HTTPException
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

users: Dict[int, Dict[str, str]] = {
    1: {"id": 1, "name": "Jamshid", "username": "john", "email": "johne@example.com"},
    2: {"id": 2, "name": "Akbar", "username": "the_akbar", "email": "theakbar@example.com"},
    3: {"id": 3, "name": "Alice", "username": "alice", "email": "alice@example.com"},
}


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str


@app.post("/user/")
def create_users(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.id] = user
    return user


@app.get("/user/{user_id}")
def get_users(user_id: int):
    user = users.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
