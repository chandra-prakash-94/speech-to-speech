from fastapi.testclient import TestClient
from main import app, get_shared_user, fake_get_shared_user

client = TestClient(app)
app.dependency_overrides[get_shared_user] = fake_get_shared_user
response = client.get('/profile')
print(response.status_code)
print(response.json())
app.dependency_overrides.clear()