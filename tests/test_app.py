"""
Tests for the main application.

These tests verify that the basic application is set up correctly.
"""


def test_health_endpoint_returns_healthy(test_client):
    """Test that health check endpoint works"""
    response = test_client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_root_endpoint_returns_success(test_client):
    """Test that root endpoint returns API information"""
    response = test_client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "Flight Delays API" in data["name"]
    assert "docs" in data
    assert "health" in data


def test_docs_endpoint_available(test_client):
    """Test that API documentation is available"""
    response = test_client.get("/docs")

    assert response.status_code == 200
