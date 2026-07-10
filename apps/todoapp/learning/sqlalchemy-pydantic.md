# SQLAlchemy & Pydantic — Q&A (todoapp)

ORM models, request/response schemas, and the session lifecycle.

---

### Q: Why have separate Pydantic schemas and SQLAlchemy models? Why not use the DB model as the request/response directly?

**A:** They solve different jobs:
- **SQLAlchemy model** → maps to the DB table (columns, types, relationships, DDL) —
  about *persistence*.
- **Pydantic schema** → defines the shape of data crossing the API boundary; validates
  request bodies (POST/PUT) and serializes responses — about the *API contract*.

Why keep them separate:
1. **Different shapes** — a create body has fewer fields than the table (no `id`,
   `created_at`); responses differ again. Lets you have `TodoCreate`, `TodoUpdate`,
   `TodoResponse`, each exposing exactly the right fields.
2. **Security** — stops over-posting (client setting `id`, `owner_id`, `is_admin`) and
   leaking columns (`hashed_password`) in responses.
3. **Validation** — Pydantic validates input *before* it hits the DB; SQLAlchemy models
   don't validate request data that way.
4. **Decoupling** — change the DB without breaking the API contract, and vice versa.

**Bridge:** Pydantic v2 `from_attributes=True` (v1 `orm_mode=True`) lets a response schema
read fields straight off a SQLAlchemy object:

```python
class TodoResponse(BaseModel):
    id: int
    title: str
    complete: bool
    model_config = ConfigDict(from_attributes=True)
```

FastAPI serializes the ORM object the route returns through the `response_model`.

**Where in the project:** Pydantic schemas vs SQLAlchemy models in `src/`.

---

### Q: What do `db.add()`, `db.commit()`, `db.refresh()` do — and why refresh after commit?

**A:**
```python
db.add(todo)      # stage as pending — NO SQL yet
db.commit()       # flush the INSERT + commit the transaction
db.refresh(todo)  # SELECT the row back to load DB-generated values
```

- **`add`** — attaches the object to the session as *pending*; the `INSERT` is **not** sent
  yet. It's emitted at **flush**, which happens as part of `commit()`.
- **`commit`** — flushes pending SQL then commits (durable/visible). By default it also
  **expires** attributes of session objects.
- **`refresh`** — re-reads the row from the DB.

**Why refresh:** your in-memory `todo` only has the fields you set. The DB generates others
— **auto `id`**, server defaults (`created_at=now()`, `complete=false`), trigger values.
Those exist only after the INSERT. Routes usually `return todo`, and the client needs the
generated `id`; without refresh you might return `id=None`.

**Follow-up:** with `expire_on_commit=True` (default), touching `todo.id` after commit
triggers a lazy SELECT anyway — `refresh` just does it explicitly/all-at-once and avoids a
surprise query or `DetachedInstanceError`. **Mirror:** `db.rollback()` discards
uncommitted changes on error.

**Where in the project:** create/update CRUD in `src/`.

---
