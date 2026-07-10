# Testing — Q&A (todoapp)

Testing FastAPI endpoints with pytest, and isolating the database.

---

### Q: How do you test a FastAPI endpoint, and how do you swap the real DB for a test DB?

**A (endpoint testing):** `pytest` is the **test runner**. The tool that *calls your routes*
is FastAPI's **`TestClient`** (`fastapi.testclient`, built on Starlette + httpx). It runs the
app **in-process** — no server, no network:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_todos():
    r = client.get("/todos")
    assert r.status_code == 200
    assert r.json() == []
```

You get real routing/validation/serialization, fast and isolated. (For `async def` tests:
`httpx.AsyncClient` + `pytest-asyncio`.)

**A (swap the DB) — `app.dependency_overrides`:** routes get the session via
`Depends(get_db)`, so tests override that dependency — no route code changes:

```python
def override_get_db():
    db = TestingSessionLocal()     # test DB (e.g. sqlite testdb.db)
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
```

This is the payoff of DI: routes depend on the abstraction (`get_db`); tests substitute an
implementation. (`testdb.db` in this project is the SQLite file used for this.)

**Structure with pytest fixtures + `conftest.py`** (shared fixtures, auto-discovered):

```python
# conftest.py
import pytest

@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)              # setup before yield, teardown after
    app.dependency_overrides.clear()  # undo so tests don't leak
```

**Follow-ups:**
- **Test isolation** — fresh DB state per test: create/drop schema (or wrap each test in a
  transaction that rolls back) in a fixture.
- **Why override, not mock the DB call?** Overriding keeps the whole real request path and
  only swaps the edge (DB) — higher fidelity, less brittle than mocking internals.

**Where in the project:** `test/` folder, `testdb.db`, `.pytest_cache`.

---
