# Environment & Dependencies — Q&A (todoapp)

Virtual environments, requirements.txt, and dependency management.

---

### Q: What is a virtual environment, and what does `requirements.txt` (and version pinning) buy you?

**A (venv):** An **isolated Python environment** — its own interpreter and `site-packages`,
so `pip install`/`python` operate inside that sandbox, not on the system Python.

Why not install globally:
- **No cross-project conflicts** — project A needs `sqlalchemy==1.4`, B needs `2.0`;
  separate venvs keep each isolated (globally they'd overwrite each other).
- **Reproducibility** — self-contained deps matching `requirements.txt`.
- **No sudo / no polluting system Python.**

Java parallel: like each project having its own dependency set instead of one shared global
classpath.

```bash
python -m venv fastapienv
source fastapienv/bin/activate   # macOS/Linux
pip install fastapi              # installs into the venv only
deactivate
```

**A (requirements.txt):** the declared dependency list — like Maven `<dependencies>` /
`package.json`. Lets anyone (teammate, CI, prod) recreate the env:

```bash
pip install -r requirements.txt   # install everything
pip freeze > requirements.txt     # snapshot exact installed versions
```

(You still use pip — the file just means one command instead of typing each package.)

**Version pinning:**
- `fastapi` (unpinned) → installs *whatever's latest* → different machines get different
  versions → "works on my machine" bugs.
- `fastapi==0.110.0` (pinned) → everyone gets the **same** version → **reproducible,
  deterministic builds** across dev/CI/prod. (`pip freeze` writes `==` pins.)

Trade-off: strict `==` is stable but you update deliberately (no auto security patches).
`>=1.0,<2.0` allows safe patches while blocking breaking majors. Modern tools (poetry,
pipenv, uv) add a **lockfile** pinning the whole transitive tree with hashes.

**Follow-ups:**
- **requirements.txt vs lockfile** — requirements often lists *direct* deps; a lockfile pins
  *every transitive* dep to exact versions/hashes → byte-for-byte reproducible.
- **Don't commit the venv folder** to git (machine-specific); commit `requirements.txt` and
  recreate from it.

**Where in the project:** `fastapienv/`, `requirements.txt`.

---
