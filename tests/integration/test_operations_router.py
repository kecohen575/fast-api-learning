from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_sum_endpoint_positive_numbers():
    """Test sum endpoint with positive numbers."""
    response = client.get("/operations/sum?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_sum_endpoint_negative_numbers():
    """Test sum endpoint with negative numbers."""
    response = client.get("/operations/sum?x=-5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": -2}
    
    response = client.get("/operations/sum?x=5&y=-8")
    assert response.status_code == 200
    assert response.json() == {"result": -3}

def test_sum_endpoint_zero():
    """Test sum endpoint with zero."""
    response = client.get("/operations/sum?x=0&y=0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_square_endpoint_positive_number():
    """Test square endpoint with a positive number."""
    response = client.get("/operations/square?number=4")
    assert response.status_code == 200
    assert response.json() == {"result": 16}

def test_square_endpoint_zero():
    """Test square endpoint with zero."""
    response = client.get("/operations/square?number=0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

def test_square_endpoint_bounds():
    """Test square endpoint with boundary values."""

    response = client.get("/operations/square?number=0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}
    
    response = client.get("/operations/square?number=1000")
    assert response.status_code == 200
    assert response.json() == {"result": 1000000}

def test_square_endpoint_out_of_bounds():
    """Test square endpoint with out-of-bounds values."""
    
    response = client.get("/operations/square?number=-1")
    assert response.status_code == 422  # (Validation error)
    
    response = client.get("/operations/square?number=1001")
    assert response.status_code == 422