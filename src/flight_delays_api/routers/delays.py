"""Delays router for flight delays endpoint."""

from fastapi import APIRouter, HTTPException, Query

from flight_delays_api.data.loader import get_delays_by_airline
from flight_delays_api.models import DelayResponse

# Create router for delays
delays_router = APIRouter(tags=["Delays"])


@delays_router.get("/delays/", response_model=list[DelayResponse])
def get_delays(
    airline_code: str = Query(..., description="Airline code to filter by"),
    limit: int = Query(
        default=50,
        ge=1,
        le=50,
        description="Maximum number of results to return (1-50)",
    ),
):
    """
    Get flight delays for a specific airline.

    Args:
        airline_code: The airline code to filter by (case-insensitive)
        limit: Maximum number of results to return (default 50, range 1-50)

    Returns:
        List of delay records matching the airline code, sorted by created_at

    Raises:
        HTTPException: 404 if no delays found for the airline, 422 for invalid params
    """
    results = get_delays_by_airline(airline_code, limit)

    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No delays found for airline: {airline_code}",
        )

    return results

