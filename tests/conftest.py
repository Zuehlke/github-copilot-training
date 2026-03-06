"""
Pytest configuration and shared test fixtures.

This module provides fixtures used across multiple test files.
"""

import pytest
from fastapi.testclient import TestClient

from flight_delays_api import app


@pytest.fixture(scope="function")
def test_client():
    """
    Provide a test client for making HTTP requests to the API in tests.

    Usage in tests:
        def test_health(test_client):
            response = test_client.get("/health")
            assert response.status_code == 200
    """

    client = TestClient(app, base_url="http://testserver")
    yield client
