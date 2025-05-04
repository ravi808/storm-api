from fastapi.testclient import TestClient
from main import app

# Create a test client using the FastAPI app
client = TestClient(app)

def test_generate_outline_success():
    """
    Test the /generate-outline endpoint with a valid topic.
    Expects:
    - HTTP 200 OK status code
    - Response contains the 'outline' key
    """
    response = client.post("/api/v1/generate-outline", json={"topic": "Climate Change"})
    assert response.status_code == 200
    assert "outline" in response.json()

def test_generate_outline_empty():
    """
    Test the /generate-outline endpoint with an empty topic.
    Expects:
    - HTTP 422 Unprocessable Entity due to validation error
    """
    response = client.post("/api/v1/generate-outline", json={"topic": ""})
    assert response.status_code == 422
