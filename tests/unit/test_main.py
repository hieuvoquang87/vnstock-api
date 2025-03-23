from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root(client):
    """Test the root endpoint returns the expected data."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "VNStock API" in data["message"]
    assert "version" in data
    assert "documentation" in data
    
def test_docs_endpoint(client):
    """Test the OpenAPI documentation endpoint is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"] 