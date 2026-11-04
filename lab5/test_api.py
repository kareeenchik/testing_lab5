import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

USER_KEYS = {"id", "name", "username", "email", "address", "phone", "website", "company"}


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    user = response.json()
    assert set(user.keys()) == USER_KEYS
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"
    assert "@" in user["email"]


def test_create_user():
    payload = {"name": "Karina Test", "username": "karina", "email": "karinka@gmail.com"}
    response = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)

    assert response.status_code == 201

    user = response.json()
    assert isinstance(user["id"], int)
    assert user["name"] == payload["name"]
    assert user["email"] == payload["email"]


def test_update_user():
    payload = {"id": 1, "name": "Karina Updated", "username": "karina", "email": "karinka@gmail.com"}
    response = requests.put(f"{BASE_URL}/users/1", json=payload, timeout=10)

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert user["name"] == payload["name"]
    assert user["email"] == payload["email"]
