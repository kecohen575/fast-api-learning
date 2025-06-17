from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_endpoint():
    payload = {"problem": "2 + 3 * 4", "round_result": False}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 14.0}

def test_calculate_with_rounding():
    payload = {"problem": "10 / 3", "round_result": True, "precision": 2}
    response = client.post("/calculate/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"solution": 3.33}
