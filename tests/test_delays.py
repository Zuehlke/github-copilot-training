"""Tests for the delays endpoint."""


def test_get_delays_requires_airline_code(test_client):
    """Test that airline_code query parameter is required."""
    response = test_client.get("/delays/")
    assert response.status_code == 422


def test_get_delays_returns_200_with_valid_airline(test_client):
    """Test that GET /delays/ returns 200 with valid airline code."""
    response = test_client.get("/delays/?airline_code=SWISS")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    # Verify all expected fields are present
    required_fields = {
        "id",
        "flight_number",
        "airline",
        "scheduled_time",
        "actual_time",
        "status",
        "delay_minutes",
        "created_at",
    }
    for record in data:
        assert set(record.keys()) == required_fields


def test_get_delays_case_insensitive_match(test_client):
    """Test that airline code matching is case-insensitive."""
    response_upper = test_client.get("/delays/?airline_code=SWISS")
    response_lower = test_client.get("/delays/?airline_code=swiss")
    response_mixed = test_client.get("/delays/?airline_code=SwIsS")

    assert response_upper.status_code == 200
    assert response_lower.status_code == 200
    assert response_mixed.status_code == 200

    upper_data = response_upper.json()
    lower_data = response_lower.json()
    mixed_data = response_mixed.json()

    assert len(upper_data) == len(lower_data) == len(mixed_data)
    # Verify same records are returned
    assert upper_data == lower_data == mixed_data


def test_get_delays_returns_404_for_unknown_airline(test_client):
    """Test that 404 is returned when no delays match the airline."""
    response = test_client.get("/delays/?airline_code=UNKNOWN_XYZ")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "UNKNOWN_XYZ" in data["detail"]


def test_get_delays_limit_enforced(test_client):
    """Test that limit parameter restricts the number of results."""
    response = test_client.get("/delays/?airline_code=SWISS&limit=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


def test_get_delays_limit_below_min_rejected(test_client):
    """Test that limit < 1 returns 422."""
    response = test_client.get("/delays/?airline_code=SWISS&limit=0")
    assert response.status_code == 422


def test_get_delays_limit_above_max_rejected(test_client):
    """Test that limit > 50 returns 422."""
    response = test_client.get("/delays/?airline_code=SWISS&limit=51")
    assert response.status_code == 422


def test_get_delays_sorted_by_created_at(test_client):
    """Test that results are sorted by created_at in ascending order."""
    response = test_client.get("/delays/?airline_code=SWISS")
    assert response.status_code == 200
    data = response.json()

    if len(data) > 1:
        # Verify created_at values are in ascending order
        created_at_values = [record["created_at"] for record in data]
        assert created_at_values == sorted(created_at_values)


def test_get_delays_returns_full_record_fields(test_client):
    """Test that response includes all required fields with correct types."""
    response = test_client.get("/delays/?airline_code=SWISS&limit=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1

    record = data[0]
    assert isinstance(record["id"], int)
    assert isinstance(record["flight_number"], str)
    assert isinstance(record["airline"], str)
    assert isinstance(record["scheduled_time"], str)  # ISO format datetime
    assert record["actual_time"] is None or isinstance(record["actual_time"], str)
    assert isinstance(record["status"], str)
    assert record["delay_minutes"] is None or isinstance(record["delay_minutes"], int)
    assert isinstance(record["created_at"], str)  # ISO format datetime


