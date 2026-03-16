"""Data loading utilities for the flight delays API."""

import json
from datetime import datetime
from pathlib import Path


def get_delays_by_airline(airline_code: str, limit: int) -> list[dict]:
    """
    Get flight delays for a specific airline, sorted by created_at.

    Args:
        airline_code: The airline code to filter by (case-insensitive)
        limit: Maximum number of records to return

    Returns:
        List of delay records matching the airline code, sorted by created_at ascending
    """
    # Resolve path to flights.json
    data_file = Path(__file__).parents[3] / "data" / "flights.json"

    # Read and parse JSON
    with open(data_file) as f:
        flights = json.load(f)

    # Filter by airline (case-insensitive)
    filtered = [
        record
        for record in flights
        if record["airline"].lower() == airline_code.lower()
    ]

    # Sort by created_at ascending
    filtered.sort(key=lambda x: datetime.fromisoformat(x["created_at"]))

    # Apply limit
    return filtered[:limit]

