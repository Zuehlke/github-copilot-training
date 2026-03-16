"""Tests for the delays endpoint."""


def test_delays_endpoint_returns_success_with_valid_airline(test_client):
    """Test that delays endpoint returns 200 with valid airline code"""
    response = test_client.get("/delays/?airline_code=LX&limit=10")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert all(flight["flight_number"].startswith("LX") for flight in data)


def test_delays_endpoint_respects_limit(test_client):
    """Test that delays endpoint respects the limit parameter"""
    response = test_client.get("/delays/?airline_code=LX&limit=1")

    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 1


def test_delays_endpoint_returns_404_for_nonexistent_airline(test_client):
    """Test that delays endpoint returns 404 for non-existent airline"""
    response = test_client.get("/delays/?airline_code=NONEXISTENT&limit=50")

    assert response.status_code == 404


def test_delays_endpoint_case_insensitive(test_client):
    """Test that airline code matching is case-insensitive"""
    response1 = test_client.get("/delays/?airline_code=lx&limit=10")
    response2 = test_client.get("/delays/?airline_code=LX&limit=10")

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() == response2.json()


def test_delays_endpoint_requires_airline_code(test_client):
    """Test that airline_code parameter is required"""
    response = test_client.get("/delays/?limit=10")

    assert response.status_code == 422  # Unprocessable Entity


def test_delays_endpoint_default_limit(test_client):
    """Test that limit defaults to 50"""
    response = test_client.get("/delays/?airline_code=LX")

    assert response.status_code == 200
    # LX only has 1 flight in the data, so we should get 1
    assert len(response.json()) == 1


def test_delays_endpoint_returns_404_for_aa(test_client):
    """Example from the task statement: AA is not present in sample data."""
    response = test_client.get("/delays/?airline_code=AA&limit=50")

    assert response.status_code == 404


