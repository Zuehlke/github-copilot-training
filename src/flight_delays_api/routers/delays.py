"""Router for delay-related endpoints."""

import json
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query

from flight_delays_api.models.delay import Delay

DATA_FILE = Path(__file__).resolve().parents[3] / "data" / "flights.json"

delays_router = APIRouter(prefix="/delays", tags=["Delays"])


def _load_delayed_flights() -> list[Delay]:
    """Load delayed flights from the bundled sample data file."""
    with DATA_FILE.open("r", encoding="utf-8") as data_file:
        flights = json.load(data_file)

    return [
        Delay.model_validate(flight)
        for flight in flights
        if flight.get("status") == "DELAYED"
    ]


@delays_router.get("", response_model=list[Delay])
@delays_router.get("/", response_model=list[Delay], include_in_schema=False)
def get_delays(
    airline_code: str | None = Query(default=None, min_length=2),
    limit: int | None = Query(default=None, ge=1),
) -> list[Delay]:
    """Return delayed flights, optionally filtered by airline code and limit."""
    delays = _load_delayed_flights()

    if airline_code:
        normalized_code = airline_code.strip().upper()
        delays = [
            delay
            for delay in delays
            if delay.flight_number.upper().startswith(normalized_code)
        ]

    if limit is not None:
        delays = delays[:limit]

    if not delays:
        raise HTTPException(status_code=404, detail="No delays found")

    return delays


