"""API routers for the flight delays API."""

from flight_delays_api.routers.delays import delays_router
from flight_delays_api.routers.health import health_router
from flight_delays_api.routers.main import main_router

__all__ = ["delays_router", "health_router", "main_router"]
