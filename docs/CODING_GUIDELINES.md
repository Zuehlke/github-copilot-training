# Coding Guidelines

These guidelines are derived from the current repository setup and source code.

## Source of Truth

- Project metadata and dependencies: `pyproject.toml`
- Lint/format behavior: `.ruff.toml`
- Standard developer commands: `Taskfile.yml`
- Existing code and tests: `src/` and `tests/`

## Code Style and Formatting

- Use Ruff as configured in `.ruff.toml`; do not introduce ad-hoc style rules.
- Run formatting via task command:

```bash
task format
```

- Run lint checks (or auto-fix where possible):

```bash
task lint
task lint-fix
```

- Prefer adding/maintaining type-aware Pydantic models for API payloads and responses (pattern used in `src/flight_delays_api/models/health.py`).

## Naming and Organization Patterns

- Keep FastAPI routers in `src/flight_delays_api/routers/`.
- Name router instances with `_router` suffix (for example `main_router`, `health_router`).
- Group Pydantic models in `src/flight_delays_api/models/` and use descriptive response names (for example `HealthResponse`).
- Register shared exports in package `__init__.py` files using `__all__` (pattern used in `models/__init__.py`, `routers/__init__.py`).

## Command Execution

Use `task` commands from `Taskfile.yml` instead of raw one-off commands where possible.

## Testing Conventions

- Tests live under `tests/` and are discovered via `pyproject.toml` pytest settings.
- Reuse shared fixtures through `tests/conftest.py` (`test_client` fixture pattern).
- Validate endpoint behavior via HTTP responses and JSON payload assertions (`tests/test_app.py`).

## Security and Reliability Practices Observed

- Dependency versions are constrained in `pyproject.toml` and locked in `uv.lock`.
- Request/response validation handling is centralized in `src/flight_delays_api/exceptions.py`.
- Response validation failures return a generic `500` detail message instead of exposing raw internals.
- No authentication or authorization layer is currently present in the codebase; treat any new data endpoints accordingly.
