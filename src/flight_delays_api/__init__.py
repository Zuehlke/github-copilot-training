"""Main Application.

This module sets up the FastAPI application.
"""

import logging

from fastapi import FastAPI

from flight_delays_api.exceptions import setup_exception_handlers
from flight_delays_api.routers import main_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Flight Delays API",
    description="API for managing flight delay information",
    version="0.1.0",
    docs_url="/docs",
)

# Include routers
app.include_router(main_router)

# Setup exception handlers
setup_exception_handlers(app)
