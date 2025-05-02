from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_outline_success():
    response = client.post("/api/v1/generate-outline", json={"topic": "Climate Change"})
    assert response.status_code == 200
    assert "outline" in response.json()

def test_generate_outline_empty():
    response = client.post("/api/v1/generate-outline", json={"topic": ""})
    assert response.status_code == 422
