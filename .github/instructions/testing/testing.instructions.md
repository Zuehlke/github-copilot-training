---
applyTo: "tests/**/*.py"
---

# Testing Philosophy
- Follow Test-Driven Development (TDD).
- **Test behavior**, not internal implementation.
- Each test should verify **one clear outcome**.
- Tests must be **independent** and runnable in any order.
- Use **clear, descriptive names** explaining the scenario and result.

# Test Organization

## File Structure

```
tests/
├── conftest.py          # Shared fixtures
├── test_items.py        # Tests for items router
└── data/                # Optional test data files
```

## Naming Conventions

| Element | Convention |
|---|---|
| Test file | `test_<module_name>.py` |
| Test function | `test_<feature>_<scenario>_<expected_result>` |
| Test class (optional) | `Test<FeatureName>` |

### Examples

```python
def test_get_items_returns_200_when_data_exists()
def test_get_items_returns_404_when_no_data()
def test_get_items_filters_by_status()
def test_item_model_validates_status()
```

# Test Fixtures (conftest.py)

Use fixtures for reusable setup logic.

```python
import pytest
from fastapi.testclient import TestClient

from function_app import app

@pytest.fixture(scope="function")
def test_client():
    """Provide a FastAPI test client"""
    client = TestClient(app)
    yield client


@pytest.fixture
def sample_item():
    """Single test item"""
    return {
        "id": "ITEM123",
        "name": "Sample item",
        "status": "active",
        "created_at": "2024-02-28T10:00:00Z"
    }


@pytest.fixture
def sample_items_list():
    """List of test items"""
    return [
        {"id": "ITEM123", "name": "Item A", "status": "active"},
        {"id": "ITEM456", "name": "Item B", "status": "inactive"},
        {"id": "ITEM789", "name": "Item C", "status": "active"},
    ]
```

# API Endpoint Testing

## GET Endpoints

```python
def test_get_items_success_returns_200(test_client):
    """GET /items returns 200 when data exists"""

    # Arrange

    # Act
    response = test_client.get("/items")

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert "count" in data
    assert "results" in data
    assert data["count"] > 0
```

```python
def test_get_items_not_found_returns_404(test_client):
    response = test_client.get("/items")

    assert response.status_code == 404
    assert "detail" in response.json()
```

```python
def test_get_items_filters_by_status(test_client):
    response = test_client.get("/items?status=active")

    assert response.status_code == 200

    results = response.json()["results"]
    assert all(r["status"] == "active" for r in results)
```

```python
def test_get_items_respects_limit_parameter(test_client):
    response = test_client.get("/items?limit=10")

    assert response.status_code == 200

    results = response.json()["results"]
    assert len(results) == 10
```

## POST Endpoints

```python
def test_create_item_success_returns_201(test_client):

    new_item = {
        "id": "ITEM123",
        "name": "Sample item",
        "status": "active"
    }

    response = test_client.post("/items", json=new_item)

    assert response.status_code == 201

    data = response.json()
    assert data["id"] == "ITEM123"
    assert "id" in data
```

```python
def test_create_item_invalid_data_returns_422(test_client):

    invalid_item = {
        "id": "ITEM123",
        "status": "active"
    }

    response = test_client.post("/items", json=invalid_item)

    assert response.status_code == 422
```

# Parametrized Testing

Use parametrization for multiple test scenarios.

```python
@pytest.mark.parametrize(
    "status,expected_count",
    [
        ("active", 2),
        ("inactive", 1),
        ("archived", 0),
    ],
)
def test_filter_by_status_parametrized(test_client, status, expected_count):

    response = test_client.get(f"/items?status={status}")

    if expected_count == 0:
        assert response.status_code == 404
    else:
        assert response.status_code == 200
        assert response.json()["count"] == expected_count
```

# Best Practices

## Arrange – Act – Assert

Structure every test in three phases.

```python
def test_example():

    # Arrange
    data = {"key": "value"}

    # Act
    result = function_under_test(data)

    # Assert
    assert result == expected_value
```

## Test Independence

### ❌ Avoid

Tests depending on execution order.

```python
def test_create_user():
    user = create_user("test@example.com")

def test_update_user():
    user = get_user("test@example.com")
```

### ✅ Prefer

Each test prepares its own data.

```python
def test_create_user():
    user = create_user("test@example.com")

def test_update_user():
    user = create_user("test@example.com")
```

## Descriptive Assertions

Prefer meaningful assertions.

### ❌ Avoid

```python
assert len(results) == 3
```

### ✅ Prefer

```python
assert len(results) == 3, f"Expected 3 items, got {len(results)}"
```

Or:

```python
assert response.status_code == 200
assert "results" in response.json(), "Response missing 'results' key"
```

# Test Completion Checklist

Before finishing tests ensure:

- [ ] File follows naming convention (`test_*.py`)
- [ ] Test names are descriptive
- [ ] Arrange‑Act‑Assert structure used
- [ ] Tests are independent
- [ ] Success and error cases tested
- [ ] Shared setup implemented with fixtures
- [ ] All tests pass (`task test`)
- [ ] No skipped tests without justification