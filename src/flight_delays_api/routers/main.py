"""Main API router."""

from fastapi import APIRouter, HTTPException, Query

from flight_delays_api.data import load_flights_data
from flight_delays_api.models import DelayResponse

# Create router for main endpoints
main_router = APIRouter(tags=["Main"])


@main_router.get("/")
def root():
    """Root endpoint - returns API information."""
    return {
        "name": "Flight Delays API",
        "version": "0.1.0",
        "status": "operational",
        "docs": "/docs",
        "health": "/health",
    }


@main_router.get("/delays/", response_model=list[DelayResponse])
def get_delays(
    airline_code: str = Query(..., min_length=2, description="Two-letter airline code"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
):
    """Get flight delays for a specific airline."""
    flights = load_flights_data()

    normalized_airline_code = airline_code.strip().upper()

    # Airline code is derived from the first 2 chars of the flight number (e.g., LX100 -> LX).
    filtered_flights = [
        flight
        for flight in flights
        if str(flight.get("flight_number", "")).upper().startswith(normalized_airline_code)
    ]

    # Return 404 if no flights found for the airline code.
    if not filtered_flights:
        raise HTTPException(status_code=404, detail="No flights found for the specified airline code")

    # Apply limit
    return filtered_flights[:limit]


