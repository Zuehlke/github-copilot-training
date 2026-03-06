---
applyTo: "**/*.py"
---

# Development methodology
- Follow Test-Driven Development (TDD).
- Tests are defined in `.github/instructions/tests.md` and must be implemented before the corresponding functionality.
- Prefer small, isolated units with clear boundaries (pure functions where possible).

# Code Style
## Python Style
- Follow PEP 8.
- Use type hints for all functions and public methods.
- Max line length: 120 characters.
- Use descriptive variable names; avoid abbreviations unless standard.
- Apply clean code principles; refactor when smells appear.

## Naming Conventions
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- “Private” members: prefix with `_`

## Import Organization
- Group imports: standard library, third-party, local.
- Keep imports sorted and avoid unused imports.
```python
# Standard library
import os
from datetime import datetime

# Third-party
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Local
from function_app.models import Item
from function_app.dependencies import get_session
```

# API Endpoint Design

- Use plural resource names (`/items`, not `/item`).
- Follow REST conventions for endpoint behavior.

## HTTP Status Codes

Use appropriate HTTP status codes:

- `200 OK` — successful read/update operations
- `400 Bad Request` — invalid request input not covered by validation
- `401 Unauthorized` — authentication required
- `404 Not Found` — resource does not exist
- `500 Internal Server Error` — unexpected system error

## Query Parameters

- Use query parameters for filtering, pagination, and optional inputs. 

Example:

```GET /items?status=active&limit=50&offset=0```

## Error Handling

- Never expose internal stack traces or sensitive system details.
- Use HTTPException for expected API errors.
- Map domain errors to appropriate HTTP status codes.
- Log unexpected errors with sufficient context for debugging.

Example:
```python
from fastapi import HTTPException

if not results:
    raise HTTPException(status_code=404, detail="No items found")
```

## Response Structure

- Responses should be consistent across endpoints.

# Common Patterns
## Router Implementation
- Use FastAPI routers for modular API design.

Example:
```python
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/items")
def get_items(
    status: str | None = None,
    limit: int = 100,
    session=Depends(get_session)
):
    # Implementation
    ...
```

## Model Implementation
- Use Pydantic models for request and response validation.

Example:
```python
from pydantic import BaseModel, Field
from datetime import datetime

class Item(BaseModel):
    id: str = Field(..., description="Item identifier")
    name: str = Field(..., description="Item name")
    created_at: datetime
```

