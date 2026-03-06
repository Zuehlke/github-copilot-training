"""Health check router."""

from datetime import datetime, timezone

from fastapi import APIRouter

from flight_delays_api.models import HealthResponse

# Create router for health
health_router = APIRouter(tags=["Health"])


@health_router.get("/health", response_model=HealthResponse)
def health_check():
    """
    Health check endpoint.

    Returns:
        Health status with timestamp and version
    """
    return HealthResponse(status="healthy", timestamp=datetime.now(timezone.utc))
