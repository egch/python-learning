# Python Core — Q&A (todoapp)

Language fundamentals that come up regardless of framework.

---

### Q: List vs tuple — and why can a tuple be a dict key / set member but not a list?

**A:** **List** — mutable, dynamic (`[1, 5, "enrico"]`, defined with `[]`); append/remove/
reassign allowed. **Tuple** — immutable (`(1, 2, 3)`, defined with `()`); can't change
after creation.

Semantic intent: a list is usually a *collection of similar things* of unknown length; a
tuple is often a *fixed record of related-but-different things* where position has meaning
(e.g. `(lat, lon)`).

**Dict-key / set trap — hashability:** keys and set members must be **hashable** (stable
`__hash__()` for their lifetime).
- A list is mutable → its hash could change → forbidden; lists have `__hash__ = None`, so
  `hash([1,2])` raises `TypeError: unhashable type: 'list'`.
- A tuple is immutable → stable hash → valid key.

```python
d = {(0, 0): "origin"}   # ✅
d = {[0, 0]: "origin"}   # ❌ TypeError: unhashable type: 'list'
```

**Follow-up — is a tuple always hashable? No.** Only if *all its elements* are hashable:

```python
hash((1, 2, 3))      # ✅
hash((1, [2, 3]))    # ❌ contains a mutable list
```

So "immutable" ≠ "hashable" — the tuple's structure is fixed, but its hash depends on its
contents.

---

### Q: What is a decorator in Python? (and is it like a Java annotation?)

**A:** ⚠️ **Not** like a Java annotation. A Java annotation is *passive metadata* read later
via reflection. A Python decorator is **active code that runs at definition time and
actually wraps/replaces the function.**

A decorator is a **callable that takes a function and returns a (new) function.** `@` is
sugar:

```python
@my_decorator
def greet(): ...
# equivalent to:
greet = my_decorator(greet)
```

Simple example:

```python
import functools

def log_calls(func):
    @functools.wraps(func)            # preserves name/docstring
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"done {func.__name__}")
        return result
    return wrapper

@log_calls
def add(a, b): return a + b
```

`*args/**kwargs` pass any arguments through; `functools.wraps` keeps `add.__name__` correct.

**FastAPI nuance:** `@app.get("/todos")` has parentheses → it's a **decorator factory**.
`app.get("/todos")` is called first and *returns* the real decorator, which wraps the route
and **registers it in the routing table**. Real work at import time, not metadata.

**Follow-up — why parens in `@app.get(...)` but not `@log_calls`?** With args you need a
factory (outer call captures args, returns the decorator); without args the decorator gets
the function directly.

**Where in the project:** `@app.get/post/put/delete` (or `@router.*`) on every route.

---

### Q: The mutable default argument trap — `def add_todo(item, todos=[])`

**A:** The default `[]` is evaluated **once at definition time**, not per call, so that one
list is **shared across all calls** that don't pass their own:

```python
add_todo("a")   # → ["a"]
add_todo("b")   # → ["a", "b"]   😱 not ["b"]
```

Defaults are stored on the function object (`add_todo.__defaults__`); mutating one
(`.append`) mutates the shared, persistent object.

**Rule:** never use a mutable default (`[]`, `{}`, `set()`). **Fix** with a `None` sentinel:

```python
def add_todo(item, todos=None):
    if todos is None:
        todos = []       # fresh per call
    todos.append(item)
    return todos
```

**Same trap in Pydantic** — use `default_factory`, not `= []`:

```python
from pydantic import BaseModel, Field
class Todo(BaseModel):
    tags: list[str] = Field(default_factory=list)  # fresh list per instance
```

**Where in the project:** Pydantic schemas with list/dict fields.

---

### Q: `==` vs `is`, and why `if todo is None:`?

**A:** (Common mix-up — neither is about `isinstance`.)
- **`==`** → **value/equality**; calls `__eq__`, which a class can define.
- **`is`** → **identity**; are both names the same object in memory (`id()`)? No method
  call — a pointer comparison.

```python
a = [1,2,3]; b = [1,2,3]
a == b   # True  (same contents)
a is b   # False (different objects)
```

**Why `is None`:**
1. `None` is a **singleton** — exactly one in the process; the right question is identity.
   (PEP 8 idiom.)
2. `==` can be **overridden/lie** — a custom `__eq__` may misbehave, raise, or (NumPy/pandas)
   return a non-bool. `is` bypasses all that.
3. Faster, unambiguous.

Same for `is True`/`is False` and singletons generally.

**Follow-up:** `256 is 256` is True but `257 is 257` may be False → CPython **interns** small
ints (-5..256) and short strings. Implementation detail — never rely on it; use `==` for
values.

**Where in the project:** `if todo is None:` guards in the routes.

---

### Q: What is the GIL, and what does it mean for CPU-bound vs I/O-bound work?

**A:** The **GIL (Global Interpreter Lock)** is a mutex in **CPython** that lets only **one
thread execute Python bytecode at a time** per process. So plain threads can't run Python
code truly in parallel across cores. It exists to keep reference-counting memory management
thread-safe; it's a CPython implementation detail, not part of the language.

**Consequences:**
- **CPU-bound** (number crunching): threads **don't help** — use **`multiprocessing`**
  (separate processes, each own GIL) or C/NumPy code that releases the GIL.
- **I/O-bound** (DB, HTTP, files): the GIL is **released while waiting on I/O**, so threads
  **do** help — one thread waits while another runs. This is why FastAPI's threadpool for
  `def` routes works fine.

**Ties to the app:** a todo app is I/O-bound (waiting on Postgres/network), so the GIL is
mostly a non-issue. `async`/`await` handles I/O concurrency on a single thread (no GIL
contention). To use many CPU cores in prod, run **multiple worker processes**
(`uvicorn --workers 4` / Gunicorn), not threads.

**Follow-up:** use all cores → multiprocessing / C extensions. Threads = I/O concurrency,
processes = CPU parallelism. (CPython 3.13+ has an experimental free-threaded/no-GIL build;
default still has the GIL.)

**Where in the project:** deployment (uvicorn workers) + async vs sync routes.

---

### Q: List comprehension vs generator expression, and what is a generator (`yield`)?

**A:** Difference is `[]` vs `()`:

```python
[x*x for x in range(1_000_000)]   # builds the WHOLE list in memory now
(x*x for x in range(1_000_000))   # lazy generator — builds nothing yet
```

- **List comprehension** — computes *all* values immediately, stores them in memory.
- **Generator expression** — **lazy**: computes one value at a time, on demand; near-zero
  memory (just current position).

**A generator** produces values lazily via `yield`. Calling it returns a **generator
object**; each iteration runs to the next `yield`, returns that value, and **pauses keeping
local state** until asked again:

```python
def count_up(n):
    i = 0
    while i < n:
        yield i      # pause, return i, resume on next()
        i += 1
```

**Why yield one at a time:**
1. **Memory** — never materialize the whole sequence (process a 10 GB file line by line).
2. **Lazy / short-circuit** — values computed only if consumed; `break` early → rest never
   computed.
3. **Composability** — pipe generators into streaming pipelines.

**Which to use:** need values more than once / `len()` / indexing → **list**. Iterate once
over something large → **generator**.

**Ties to the app:** `get_db` uses `yield` — a **generator dependency**. Same mechanism: it
pauses at `yield db`, hands the session to FastAPI, and resumes to run `db.close()` after
the request.

**Follow-up — iterable vs iterator vs generator:** *iterable* = loopable (`__iter__`, e.g. a
list); *iterator* = produces values one by one (`__next__`); *generator* = easiest way to
create an iterator — `yield` writes the plumbing for you.

**Where in the project:** `get_db` generator dependency.

---

### Q: `__str__` vs `__repr__` — when is each called, and which to implement if only one?

**A:** Both return a string representation, different audiences:
- **`__repr__`** → **developers**. Unambiguous, ideally recreatable Python. Used by the
  **REPL, debugger, and containers** (list/dict).
- **`__str__`** → **end users**. Readable/pretty. Used by `print(obj)` and `str(obj)`.

```python
class Todo:
    def __init__(self, id, title): self.id, self.title = id, title
    def __repr__(self): return f"Todo(id={self.id!r}, title={self.title!r})"
    def __str__(self):  return f"Todo #{self.id}: {self.title}"

print(t)   # __str__  → Todo #1: Buy milk
t          # __repr__ → Todo(id=1, title='Buy milk')  (REPL)
[t]        # __repr__ → [Todo(id=1, title='Buy milk')] (containers use repr!)
```

**Implement `__repr__` if only one** — `__str__` falls back to `__repr__`, not vice versa.
Without `__repr__` you get the useless `<Todo object at 0x...>`.

**Key detail:** containers always use `__repr__`, even if `__str__` exists.

**Ties to the app:** a good `__repr__` on SQLAlchemy models makes logs/debugging readable
(`Todo(id=1, title='Buy milk')` instead of `<Todo object at 0x...>`).

**Follow-up:** `!r` in an f-string applies `repr()` to that value (strings show quoted) —
what you want inside `__repr__`.

**Where in the project:** `__repr__` on ORM model classes in `src/`.

---
