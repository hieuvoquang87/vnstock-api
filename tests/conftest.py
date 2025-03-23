import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

@pytest.fixture
def client():
    """Return a TestClient for the FastAPI application."""
    with TestClient(app) as test_client:
        yield test_client 