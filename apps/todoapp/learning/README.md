# Learning — Python Q&A (todoapp)

Interview-prep Q&A about Python and the stack used in this app
(FastAPI + SQLAlchemy + Pydantic + Alembic). Answers are grounded in this project's code.

## Topics

- [python-core.md](python-core.md) — language fundamentals (list vs tuple, decorators,
  mutable defaults, `==` vs `is`, the GIL)
- [fastapi.md](fastapi.md) — dependency injection, `def` vs `async def`, HTTPException / 404s
- [sqlalchemy-pydantic.md](sqlalchemy-pydantic.md) — ORM models vs schemas, session
  lifecycle (`add`/`commit`/`refresh`)
- [alembic.md](alembic.md) — schema migrations
- [auth.md](auth.md) — password hashing (bcrypt) and JWT auth
- [rest-http.md](rest-http.md) — HTTP methods, idempotency, status codes
- [testing.md](testing.md) — TestClient, pytest fixtures, DB override
- [environment.md](environment.md) — virtual envs, requirements.txt, dependencies

## How to use

- Add each new question to the file matching its topic.
- Keep answers short; tie them to a file/line in `apps/todoapp` when possible.
- Prefer "why is it done this way here" over generic textbook explanations.
