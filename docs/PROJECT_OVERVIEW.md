# Project Overview

## Purpose

`flight-delays-api` is a small FastAPI training project for managing flight delay information.

## Environment

- Python: `>=3.12` (`pyproject.toml`)
- Dependency/tooling workflow: `uv` (`Taskfile.yml`, `uv.lock`)
- Task runner: `task` (`Taskfile.yml`)
- API framework/runtime: FastAPI + Uvicorn (`pyproject.toml`, `Taskfile.yml`)
- Test tooling: Pytest + FastAPI `TestClient` (`pyproject.toml`, `tests/`)
- Lint/format tooling: Ruff (`.ruff.toml`, `Taskfile.yml`)

## Project Structure

```text
github-copilot-training/
|- src/flight_delays_api/
|  |- __init__.py          # FastAPI app setup and router registration
|  |- exceptions.py        # Global exception handler registration
|  |- routers/
|  |  |- main.py           # Root endpoint
|  |  `- health.py         # Health endpoint
|  `- models/
|     `- health.py         # Pydantic response model
|- tests/
|  |- conftest.py          # Shared test client fixture
|  `- test_app.py          # Endpoint smoke tests
|- data/flights.json       # Sample delay data set
|- Taskfile.yml            # Standard project commands
|- pyproject.toml          # Package metadata + dependencies
`- .ruff.toml              # Lint/format config
```

## Main Architectural Concepts

- Application entry point: `flight_delays_api:app` in `src/flight_delays_api/__init__.py`
- Router-based API composition using `APIRouter` modules under `src/flight_delays_api/routers/`
- Typed API contracts with Pydantic models in `src/flight_delays_api/models/`
- Centralized exception registration in `src/flight_delays_api/exceptions.py`
- Tests use in-process HTTP calls through `fastapi.testclient.TestClient`

## Integrations

- Runtime integration with `uvicorn` (`task run`)
- Development tooling integration with `uv` for dependency resolution and command execution (`uv sync`, `uv run ...`)
- Quality tooling integration with Ruff and Pytest tasks (`task lint`, `task format`, `task test`)
- Data integration: local JSON fixture in `data/flights.json` (no external data service configured)
