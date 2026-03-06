# Project Overview

This is the overview of a Python project using GitHub Copilot.

## Technology Stack

It uses the following technologies:

- **FastAPI** for REST endpoints with automatic API documentation
- **Uvicorn** as the ASGI web server
- **Pydantic** for data validation
- **pytest** for testing
- **ruff** for linting and formatting
- **uv** for modern package management with reproducible builds

## Project Structure

```text
github-copilot-training/
├── .ruff.toml                    # Ruff linting/formatting config
├── uv.lock                       # Locked dependencies for reproducibility
├── pyproject.toml                # Project metadata and dependencies
├── README.md                     # This file
├── src/
│   └── flight_delays_api/        # Main application
│       ├── __init__.py           # FastAPI app setup
│       ├── models/               # Pydantic models
│       └── routers/              # API endpoints
├── tests/                        # Test suite
└── data/                         # Sample data
```