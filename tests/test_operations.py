from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sum_endpoint():
    response = client.get("/operations/sum?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_square_endpoint():
    response = client.get("/operations/square?number=4")
    assert response.status_code == 200
    assert response.json() == {"result": 16}