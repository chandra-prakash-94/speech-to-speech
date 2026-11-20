##test_main.py
from fastapi.testclient import TestClient
from main import app, get_shared_user, fake_get_shared_user

client = TestClient(app)
app.dependency_overrides[get_shared_user] = fake_get_shared_user
response = client.get('/profile')
assert response.status_code==200
assert response.json()=={
    "profile":{"username":"Bob"}
}

app.dependency_overrides.clear()