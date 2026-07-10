# Alembic — Q&A (todoapp)

Database schema migrations.

---

### Q: What is Alembic, and why not just use `Base.metadata.create_all()`?

**A:** Alembic is a **schema migration** tool for SQLAlchemy — the Python equivalent of
**Flyway/Liquibase** in Java. It evolves the DB schema over time (add column, create table,
add index) in a **versioned, repeatable, reversible** way.

Each change is a **revision script** with `upgrade()` / `downgrade()`. Revisions form a
chain (`revision` + `down_revision`), and Alembic records applied ones in an
`alembic_version` table, so every environment applies only what it's missing.

**Why not `create_all()`:** it only *creates tables that don't exist yet* — it **never
alters an existing table**. In production with real data:
- Add a `due_date` column → table already exists → `create_all()` does nothing, column
  never appears.
- Can't rename columns, change types, add constraints, or drop things.
- No history, no rollback.
- Only way to "refresh" schema with create_all is drop + recreate → **data loss**.

Alembic gives incremental `ALTER`s, history, rollback, and cross-env reproducibility.

```bash
alembic revision --autogenerate -m "add due_date"   # draft from model diff
alembic upgrade head      # apply pending
alembic downgrade -1      # roll back last
alembic current / history # where am I / the chain
```

**Follow-up:** `--autogenerate` diffs models vs DB and drafts the migration, but **review
it** — it misses some constraint changes, treats renames as drop+add, and doesn't handle
data migrations.

**Where in the project:** `alembic/` + `alembic.ini`.

---
