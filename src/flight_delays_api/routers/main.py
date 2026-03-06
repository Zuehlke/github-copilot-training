"""Main API router."""

from fastapi import APIRouter

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
