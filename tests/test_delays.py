"""Tests for delay endpoints."""


def test_get_delays_returns_delayed_flights(test_client):
    """Base /delays endpoint returns delayed flights."""
    response = test_client.get("/delays")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) > 0
    assert all(item["status"] == "DELAYED" for item in payload)


def test_get_delays_honors_limit(test_client):
    """Limit query parameter truncates response size."""
    response = test_client.get("/delays?limit=2")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 2


def test_get_delays_with_airline_code_and_limit_not_found(test_client):
    """Unknown airline code should return 404 when no delays match."""
    response = test_client.get("/delays?airline_code=AA&limit=50")

    assert response.status_code == 404
    assert response.json() == {"detail": "No delays found"}

