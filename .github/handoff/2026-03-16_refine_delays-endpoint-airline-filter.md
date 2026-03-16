# Refine Handoff: Delays endpoint with airline filter and limit

## Context & goal
The API currently exposes `/` and `/health` but no delays endpoint. Dev requested a new endpoint shape: `GET /delays/?airline_code=AA&limit=50` returning either `200 OK` or `404 Not Found`.

`airline_code` must be resolved from existing `airline` values, matching is case-insensitive, and responses should return full flight records.

## Requirements

### Must-have
- Add a read endpoint at `GET /delays/`.
- Support query params:
  - `airline_code` (required for this feature scope).
  - `limit` (optional, default `50`, minimum `1`, maximum `50`).
- Return `200 OK` with a JSON list of delay records when at least one match exists.
- Return `404 Not Found` when no records match `airline_code`.
- Sort returned records by `created_at`.
- Keep response conventions aligned with existing API style (JSON responses, FastAPI validation behavior).

### Nice-to-have
- Deterministic result ordering documented (for stable pagination/consumer behavior).
- Lightweight endpoint tests covering success, empty result, and limit behavior.

### Non-goals
- Creating/updating/deleting delays.
- Pagination model redesign beyond current `limit` parameter.
- New auth/authorization behavior.

## Constraints / Non-functional requirements
- Preserve current API compatibility for existing routes.
- Follow project command workflow (`task` targets for test/lint/format).
- Keep implementation simple (YAGNI) and avoid architectural refactors.

## Assumptions
- `airline_code` is expected as IATA-style code (example `AA`) and comparison should be case-insensitive.
- `404` applies only to "no matching airline delay records", not to malformed query params.
- If `limit` is omitted, service returns up to 50 results.
- Returned items are full flight records from the existing data source.
- `airline_code` matching is implemented via `airline` field values from current data (no new source introduced in this scope).

## Open questions / risks
- Data quality risk remains: because matching is derived from `airline` values, results depend on consistency and coverage of that field.
- Missing or malformed `airline_code` behavior still relies on FastAPI request validation defaults unless explicitly overridden.

## Acceptance criteria

1. `GET /delays/?airline_code=<code>` returns `200` and a JSON array when at least one record exists for `<code>`.
2. `airline_code` matching is case-insensitive (for example, `aa` and `AA` produce the same result set).
3. `GET /delays/?airline_code=<code>&limit=<n>` returns at most `<n>` items for `1 <= n <= 50`; invalid values outside this range fail request validation.
4. `GET /delays/?airline_code=<code>` returns `404` with a clear error payload when no records exist for `<code>`.
5. `200` responses return full flight records and are ordered by `created_at`.
6. `GET /delays/` without `airline_code` fails request validation (FastAPI standard `422`).
7. Existing endpoints (`/`, `/health`, `/docs`) continue to behave unchanged.

## Next agent must do

- [ ] Finalize plan and implement endpoint + tests based on confirmed decisions.


