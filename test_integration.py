import pytest
from main import app
from fastapi.testclient import TestClient
from core_logic import create_user, get_user, users

client = TestClient(app)


#  Integration Test
def test_create_user_and_get():
    # add user
    resp = client.post('/user/', json={"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"})
    assert resp.status_code == 200
    assert resp.json() == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # get user
    resp = client.get('/user/4')
    assert resp.status_code == 200
    assert resp.json() == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # already user add
    resp = client.post('/user/', json={"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"})
    assert resp.status_code == 400
    assert resp.json() == {"detail": "User already exists"}

    resp = client.get('/user/5')
    assert resp.status_code == 404
    assert resp.json() == {"detail": "User not found"}


# Unit test
@pytest.fixture(autouse=True)
def reset_users():
    users.clear()


def test_create_user():
    # Add a new user
    user = create_user(4, "Bekzod", "bekzod", "bekzod@gmail.com")
    assert user == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}
    assert users[4] == user

    # Try adding the same user again
    with pytest.raises(ValueError, match="User already exists"):
        create_user(4, "Bekzod", "bekzod", "bekzod@gmail.com")


def test_get_user():
    # Add a user for testing
    users[4] = {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # Retrieve the user
    user = get_user(4)
    assert user == {"id": 4, "name": "Bekzod", "username": "bekzod", "email": "bekzod@gmail.com"}

    # Try retrieving a non-existent user
    with pytest.raises(ValueError, match="User not found"):
        get_user(5)
