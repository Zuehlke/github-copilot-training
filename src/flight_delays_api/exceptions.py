"""Exception handlers for the FastAPI application."""

import json
import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError


def setup_exception_handlers(app: FastAPI) -> None:
    """Register exception handlers with the FastAPI app."""

    @app.exception_handler(RequestValidationError)
    @app.exception_handler(ValidationError)
    async def validation_exception_handler(request, exc):
        """Handle request/body validation errors."""
        exc_json = json.dumps(exc.errors() if hasattr(exc, "errors") else exc.args)
        logging.exception(f"ValidationError occurred, Error={exc}", stacklevel=1)
        return JSONResponse(exc_json, status_code=422)

    @app.exception_handler(ResponseValidationError)
    async def response_validation_exception_handler(request, exc):
        """Handle response validation errors."""
        logging.exception(f"ResponseValidationError occurred, Error={exc.errors()}", stacklevel=1)
        return JSONResponse(content={"detail": "Internal Server Error"}, status_code=500)
