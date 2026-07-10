# FastAPI — Q&A (todoapp)

FastAPI framework mechanics: dependency injection, sync vs async, error handling.

---

### Q: What does `Depends(get_db)` do, and why is `get_db` written with `yield` instead of `return`?

**A:** `Depends()` is FastAPI's **dependency injection**. You declare what a route needs
and FastAPI calls the dependency for you and injects the result — you never call
`get_db()` yourself.

- **Composable:** a dependency can itself use `Depends(...)`, so you get chains like
  `get_current_user` → `get_db`. FastAPI resolves the whole tree.
- **Testable:** override it with `app.dependency_overrides[get_db] = fake_db` to swap in
  a test DB without touching the route.

`get_db` uses `yield` because it's a **generator dependency**: code before `yield` runs
before the request (open session), the yielded value is injected, and code after `yield`
runs after the response (close session) — like a `with` block spanning the request.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db      # injected into the route
    finally:
        db.close()    # runs after the request, even on error
```

With `return` you'd have no teardown hook and would leak connections. The `try/finally`
guarantees the session closes even if the route raises.

**Where in the project:** database/session setup (`get_db`) + router functions.

---

### Q: `def` vs `async def` in a FastAPI route — and the danger of blocking inside `async def`?

**A:** ⚠️ Common misconception: `async def` does **not** return immediately or run in the
background. From the **client's view both are identical** — the caller waits for the full
response either way. The difference is purely how the *server* handles concurrency.

- **`async def`** — runs directly on the **event loop**. While you `await` non-blocking I/O,
  the loop is freed to serve other requests. This is how one worker handles thousands of
  connections. You must only `await` non-blocking work.
- **`def`** (sync) — FastAPI runs it in an **external threadpool**, so a blocking call
  inside doesn't freeze the event loop; other requests keep flowing.

**Danger — blocking inside `async def`:** a blocking call (`time.sleep`, sync SQLAlchemy
query, `requests.get`) inside `async def` blocks the **entire single-threaded event loop**,
freezing *every* concurrent request on that worker, not just the caller.

```python
@app.get("/bad")
async def bad():
    time.sleep(5)   # ❌ freezes the whole loop — all requests stall

@app.get("/fine")
def fine():
    time.sleep(5)   # ✅ threadpool — only this request waits
```

**Rule of thumb:** async library (asyncpg, async httpx) → `async def` + `await`; blocking/
sync library (classic synchronous SQLAlchemy `Session`, as used here) → plain `def`. Need a
blocking call inside `async def`? Offload with `run_in_threadpool(fn)` / `asyncio.to_thread(fn)`.

**Where in the project:** router functions using the sync `Session` from `get_db`.

---

### Q: How do you return a 404 in FastAPI, and why raise instead of `return {"error": ...}`?

**A:** Raise **`HTTPException`**:

```python
from fastapi import HTTPException, status

todo = db.query(Todo).filter(Todo.id == todo_id).first()
if todo is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
```

FastAPI turns it into HTTP `404` with body `{"detail": "Todo not found"}`. Prefer the
`status.HTTP_404_NOT_FOUND` constant over a bare `404` (self-documenting).

**Why raise, not return an error dict:**
1. **Status code is the contract** — `return {"error": ...}` still sends **200 OK**; clients/
   monitoring read that as success. Raising sets the real `404` status line.
2. **Short-circuits** — execution stops immediately; you can't fall through with a `None`.
3. **Works from deep in the stack** — a CRUD/service layer can raise and it propagates to
   FastAPI without threading errors back manually.

**Follow-ups:** success status → `@router.post(..., status_code=status.HTTP_201_CREATED)`;
global error shape → `@app.exception_handler(...)`.

**Where in the project:** delete/edit/read routes in `src/`.

---
