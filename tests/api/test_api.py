from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to MATH!"}

def test_docs_endpoint():
    """Test that the API documentation is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_openapi_schema():
    """Test that the OpenAPI schema is accessible."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    
    assert "openapi" in schema
    assert "paths" in schema
    assert "components" in schema
    
    # Add endpoints as app expands
    assert "/calculate/" in schema["paths"]
    assert "/operations/sum" in schema["paths"]
    assert "/operations/square" in schema["paths"]