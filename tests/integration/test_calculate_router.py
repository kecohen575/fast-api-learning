from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_calculate_basic_expression():
    """Test calculating a basic expression."""
    payload = {"problem": "2 + 2", "round_result": False}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 4.0}

def test_calculate_complex_expression():
    """Test calculating a more complex expression."""
    payload = {"problem": "2 + 3 * 4", "round_result": False}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 14.0}

def test_calculate_with_rounding():
    """Test calculation with rounding enabled."""
    payload = {"problem": "10 / 3", "round_result": True, "precision": 2}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 3.33}

def test_calculate_with_different_precision():
    """Test calculation with different precision levels."""

    payload = {"problem": "10 / 3", "round_result": True, "precision": 0}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 3}
    
    payload = {"problem": "10 / 3", "round_result": True, "precision": 1}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 3.3}
    
    payload = {"problem": "10 / 3", "round_result": True, "precision": 4}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 3.3333}

def test_calculate_with_invalid_expression():
    """Test error handling for invalid expressions."""
    payload = {"problem": "10 / 0", "round_result": False}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 400
    assert "Invalid expression:" in response.json()["detail"]

def test_calculate_with_invalid_characters():
    """Test error handling for expressions with invalid characters."""
    payload = {"problem": "os.system('ls')", "round_result": False}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 400
    assert "invalid characters" in response.json()["detail"]