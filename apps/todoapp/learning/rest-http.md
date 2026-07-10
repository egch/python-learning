# REST / HTTP — Q&A (todoapp)

HTTP methods, status codes, and REST semantics.

---

### Q: POST vs PUT vs PATCH, and what is idempotency?

**A:**
- **POST** = **create** a new resource (server assigns id). Not idempotent.
- **PUT** = **replace/update** an existing resource with its **full** representation.
  Idempotent.
- **PATCH** = **partial update** — send only changed fields. Usually not guaranteed
  idempotent.

| Method | Purpose | Idempotent? |
|--------|---------|-------------|
| POST   | create a new resource | ❌ |
| PUT    | replace an existing resource fully | ✅ |
| PATCH  | partially update | ⚠️ depends |

App examples:
- `POST /todos {"title":"Buy milk"}` → creates, returns new `id`.
- `PUT /todos/5 {full object}` → replaces todo 5 entirely.
- `PATCH /todos/5 {"complete":true}` → flips just that field.

**Idempotency:** making the **same request N times has the same effect as once.**
- **PUT** idempotent — same body 1× or 10× → same final state.
- **POST** not — 3 calls create 3 todos.
- **PATCH** depends — `{"complete":true}` is; "increment views" / "append tag" isn't.
- (GET and DELETE are also idempotent.)

**Why it matters:**
1. **Safe retries** — on a timeout, retrying PUT/GET/DELETE is harmless; retrying POST can
   create **duplicates** (double-order bug).
2. Caches/proxies/load balancers rely on these guarantees.

**Follow-up — make POST safe to retry?** Use an **idempotency key**: client sends a unique
key; server records it and returns the same result on retry instead of duplicating (Stripe's
model).

**Nuance:** PUT *can* create if the **client controls the id** (`PUT /todos/5` where 5
doesn't exist yet). In the server-generates-id pattern here, POST creates / PUT updates.

**Where in the project:** add / edit / delete todo routes.

---
