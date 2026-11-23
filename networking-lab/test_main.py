##test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app, get_shared_user, fake_get_shared_user

client = TestClient(app)

@pytest.fixture
def override_user():
    app.dependency_overrides[get_shared_user] = fake_get_shared_user
    yield
    print("Fixture cleanup executed")
    app.dependency_overrides.clear()

def test_profile(override_user):
    response = client.get('/profile')
    assert response.status_code==200
    assert response.json()=={
        "profile":{"username":"Bob"}
    }

def test_real_profile():
    response = client.get('/profile')
    assert response.status_code == 200
    assert response.json() == {
    "profile": {"username": "Alice"}
}