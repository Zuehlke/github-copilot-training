# Plan Handoff: Delays endpoint with airline filter and limit

## Summary of refined spec

- New `GET /delays/` endpoint with required `airline_code` and optional `limit` (1–50, default 50) query params.
- Case-insensitive match on the `airline` field in `data/flights.json`.
- `200` + JSON array on match; `404` + error payload on no match; `422` on invalid params.
- Results sorted ascending by `created_at`; limit applied after filter.
- No existing routes affected.

---

## Architectural design

### Components/modules involved

| Layer | Module | Role |
|---|---|---|
| Data | `src/flight_delays_api/data/__init__.py` | Package init |
| Data | `src/flight_delays_api/data/loader.py` | Load and filter `flights.json` |
| Model | `src/flight_delays_api/models/delay.py` | Pydantic response model |
| Router | `src/flight_delays_api/routers/delays.py` | `GET /delays/` endpoint |
| App wiring | `src/flight_delays_api/models/__init__.py` | Export `DelayResponse` |
| App wiring | `src/flight_delays_api/routers/__init__.py` | Export `delays_router` |
| App wiring | `src/flight_delays_api/__init__.py` | Register `delays_router` |

### Responsibility boundaries

- **`loader.py`** owns reading the JSON file and filtering/sorting/limiting records. It must not contain HTTP or FastAPI concerns.
- **`delays.py` router** owns only HTTP interface concerns: query param declaration, calling the loader, and raising `HTTPException(404)` when the loader returns an empty list.
- **`delay.py` model** declares the exact response schema; all fields must match the JSON record structure.

### Key interfaces/contracts

**`loader.py`** exposes one function:

```
get_delays_by_airline(airline_code: str, limit: int) -> list[dict]
```

- Loads `flights.json` once (or on every call — see note below).
- Filters records where `record["airline"].lower() == airline_code.lower()`.
- Sorts result by `created_at` ascending.
- Returns at most `limit` records as raw dicts (the router converts to model).

> **Assumption:** No caching/singleton required by this scope. Simple load-on-call is acceptable and YAGNI-compliant. If performance becomes a concern that is a separate task.

**`DelayResponse` Pydantic model** fields (matching `flights.json` structure):
- `id: int`
- `flight_number: str`
- `airline: str`
- `scheduled_time: datetime`
- `actual_time: datetime | None`
- `status: str`
- `delay_minutes: int | None`
- `created_at: datetime`

**Router endpoint** signature:

```
GET /delays/
  airline_code: str  (Query, required)
  limit: int         (Query, default=50, ge=1, le=50)
→ 200 list[DelayResponse]
→ 404 {"detail": "No delays found for airline: <code>"}
→ 422 FastAPI validation error (missing airline_code or out-of-range limit)
```

### Data flow

```
Request → FastAPI validation → delays_router.get_delays()
  → loader.get_delays_by_airline(airline_code, limit)
    → read data/flights.json
    → filter (case-insensitive airline match)
    → sort by created_at ascending
    → slice to limit
  ← list[dict]
← 404 if empty list
← 200 list[DelayResponse] if non-empty
```

### Error handling & edge cases

- **No records found**: router raises `HTTPException(status_code=404, detail="No delays found for airline: <code>")`.
- **Missing `airline_code`**: FastAPI returns `422` automatically (required Query param).
- **`limit` outside 1–50**: FastAPI returns `422` automatically (ge/le constraints).
- **File not found / corrupt JSON**: allow natural unhandled exception (not in scope; no new error handler added).

### `data/flights.json` path resolution

Resolve path in `loader.py` using `Path(__file__).parents[3] / "data" / "flights.json"`.
- `__file__` = `.../src/flight_delays_api/data/loader.py`
- `.parents[3]` = project root

---

## Files likely to change

| File | Change type |
|---|---|
| `src/flight_delays_api/data/__init__.py` | Create (empty package init) |
| `src/flight_delays_api/data/loader.py` | Create |
| `src/flight_delays_api/models/delay.py` | Create |
| `src/flight_delays_api/models/__init__.py` | Modify – add `DelayResponse` export |
| `src/flight_delays_api/routers/delays.py` | Create |
| `src/flight_delays_api/routers/__init__.py` | Modify – add `delays_router` export |
| `src/flight_delays_api/__init__.py` | Modify – import and register `delays_router` |
| `tests/test_delays.py` | Create |

---

## Test implementation plan

### Test files

- `tests/test_delays.py`

### Test methods (write tests before implementation — TDD)

| Test | Scenario | Expected |
|---|---|---|
| `test_get_delays_requires_airline_code` | `GET /delays/` | `422` |
| `test_get_delays_returns_200_with_valid_airline` | `GET /delays/?airline_code=SWISS` | `200`, list with ≥1 record, all fields present |
| `test_get_delays_case_insensitive_match` | `GET /delays/?airline_code=swiss` | `200`, same result set as `SWISS` |
| `test_get_delays_returns_404_for_unknown_airline` | `GET /delays/?airline_code=UNKNOWN_XYZ` | `404`, detail message contains airline code |
| `test_get_delays_limit_enforced` | `GET /delays/?airline_code=SWISS&limit=1` | `200`, exactly 1 record |
| `test_get_delays_limit_below_min_rejected` | `GET /delays/?airline_code=SWISS&limit=0` | `422` |
| `test_get_delays_limit_above_max_rejected` | `GET /delays/?airline_code=SWISS&limit=51` | `422` |
| `test_get_delays_sorted_by_created_at` | Multiple records (if applicable) | `created_at` values are ascending |
| `test_get_delays_returns_full_record_fields` | `GET /delays/?airline_code=SWISS` | Response item contains all expected fields |

All tests use the existing `test_client` fixture from `conftest.py`.

---

## Code implementation plan

### Source files

#### `src/flight_delays_api/data/__init__.py`
Empty package init only (no exports needed).

#### `src/flight_delays_api/data/loader.py`
- Import `json`, `pathlib.Path`.
- Define `DATA_FILE = Path(__file__).parents[3] / "data" / "flights.json"`.
- Define `get_delays_by_airline(airline_code: str, limit: int) -> list[dict]`:
  - Read and parse `DATA_FILE`.
  - Filter by `airline` field (case-insensitive).
  - Sort by `created_at` string (ISO 8601 sort is lexicographic-safe, but parse with `datetime.fromisoformat` for correctness).
  - Return `result[:limit]`.

#### `src/flight_delays_api/models/delay.py`
- Define `DelayResponse(BaseModel)` with all fields from the JSON schema.
- Nullable fields (`actual_time`, `delay_minutes`) typed as `Optional`.
- Use `Field(..., description=...)` for documented fields, following `health.py` pattern.

#### `src/flight_delays_api/routers/delays.py`
- Define `delays_router = APIRouter(tags=["Delays"])`.
- Endpoint: `@delays_router.get("/delays/", response_model=list[DelayResponse])`.
- Query params: `airline_code: str = Query(...)`, `limit: int = Query(default=50, ge=1, le=50)`.
- Call `get_delays_by_airline(airline_code, limit)`.
- Raise `HTTPException(status_code=404, detail=f"No delays found for airline: {airline_code}")` if empty result.
- Return the list (FastAPI serializes via `response_model`).

### Helpers/utilities

No new utilities beyond `loader.py`.

---

## Integration plan

- `models/__init__.py`: add `from flight_delays_api.models.delay import DelayResponse` and add `"DelayResponse"` to `__all__`.
- `routers/__init__.py`: add `from flight_delays_api.routers.delays import delays_router` and add `"delays_router"` to `__all__`.
- `flight_delays_api/__init__.py`: add `from flight_delays_api.routers import ..., delays_router` and `app.include_router(delays_router)` after existing router registrations.
- No documentation updates required (FastAPI auto-generates `/docs` from the router definition).
- No migration concerns (new endpoint, no data store changes).

---

## Validation plan

Run after implementation:

```bash
task test
task lint
task test-coverage
```

### Manual test scenarios

| Scenario | Command |
|---|---|
| Valid airline (uppercase) | `GET /delays/?airline_code=SWISS` |
| Valid airline (lowercase) | `GET /delays/?airline_code=swiss` |
| Unknown airline | `GET /delays/?airline_code=ZZZ999` |
| Limit enforced | `GET /delays/?airline_code=SWISS&limit=1` |
| Limit too high | `GET /delays/?airline_code=SWISS&limit=51` |
| Limit zero | `GET /delays/?airline_code=SWISS&limit=0` |
| Missing airline_code | `GET /delays/` |
| Existing routes unaffected | `GET /`, `GET /health`, `GET /docs` |

### Edge cases

- Airline code with mixed case (e.g., `Swiss`) must return same result as `SWISS`.
- Response items must include all fields; nullable fields must be `null` (not omitted) in JSON.
- `limit` default of 50 must not require explicit passing.

---

## Next agent must do

- [ ] Implement the plan using TDD (write tests first, then source code).
- [ ] Run `task test` and `task lint` to confirm all checks pass.
- [ ] Verify ≥80% coverage on new code with `task test-coverage`.

