"""Data loading utilities."""

import json
from pathlib import Path
from typing import Any


def load_flights_data() -> list[dict[str, Any]]:
    """Load flight data from JSON file."""
    data_path = Path(__file__).parent.parent.parent.parent / "data" / "flights.json"
    with open(data_path) as f:
        return json.load(f)

