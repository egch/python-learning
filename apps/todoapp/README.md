# Todos
You need to have a pycharm project starting from this folder!

## How to Run

### 1. Create and activate the virtual environment

**Mac/Linux**
```shell
p3 -m pip install --upgrade pip
p3 -m venv fastapienv
source fastapienv/bin/activate
```

**Windows**
```shell
python3 -m pip install --upgrade pip
python3 -m venv fastapienv
fastapienv\Scripts\activate
```

### 2. Install dependencies from requirements.txt
```shell
pip install -r requirements.txt
```

### 3. Start PostgreSQL
```shell
cd docker-compose
docker compose up -d
```

### 4. Start the app
```shell
uvicorn src.main:app --reload
```

The API will be available at http://127.0.0.1:8000
Swagger UI (interactive docs) at http://127.0.0.1:8000/docs

---

## Commands


### Generate random secret
```shell
openssl rand -hex 32
```
## sqllite

```shell
 sqlite3 todosapp.db
```

## Authentication

User `a/a` previously added in the db.

![from swagger](docs/authentication.png)



## Database

PostgreSQL runs via Docker Compose. The compose file and data volume are in the `docker-compose/` folder.

### Start Postgres
```shell
cd docker-compose
docker compose up -d
```

### Stop Postgres
```shell
cd docker-compose
docker compose down
```

### Connection details
| Field    | Value     |
|----------|-----------|
| Host     | localhost |
| Port     | 5432      |
| Database | todosapp  |
| User     | postgres  |
| Password | p123      |

**Connection URL:**
```
postgresql://postgres:p123@localhost:5432/todosapp
```

### Cleanup Docker Volume when Changing PostgreSQL Initialization

When using the official PostgreSQL Docker image, the environment variables

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

are applied **only the first time the database is initialized**.

If the database data directory already exists (for example because of a mounted volume like `./data:/var/lib/postgresql/data`), PostgreSQL **will ignore any changes to these variables**.

Therefore, if you modify the initialization configuration, you must remove the existing volume or data directory.

**Example (bind mount):**
```shell
rm -rf data  
docker compose up
```


**Example (Docker volume):**

docker compose down -v  
docker compose up

This forces PostgreSQL to initialize a **fresh database cluster with the new configuration**.

### PgAdmin
![pgAdmin.png](docs/pgAdmin.png)
## Links
[jwt io](http://www.jwt.io)

### Change Password
Use this so you remember it: `12345!`

## Alembic
```shell
alembic init alembic
```

Change the sql alchemy url in the [alembic.ini](alembic.ini) file:
```properties
sqlalchemy.url = 'postgresql://postgres:<pwd>@localhost/TodoApplicationDatabase'
```

Import your models and change some setting in [env.py](alembic/env.py).

> **Note:**  Since models live under `src/`, use `from src import models` in `env.py` (not `import models`), and keep `prepend_sys_path = .` in `alembic.ini` so that `src` is resolvable as a package from the project root.

### Create revision
```shell
alembic revision -m "Create phone number for user column"
```
Once the revision is created under the [versions](alembic/versions) folder we need to implement
these two methods:
```python
def upgrade() -> None:
    """Upgrade schema."""
    pass
  

def downgrade() -> None:
    """Downgrade schema."""
    pass
```

Running upgrade. Revision ID is defined in the revision file under the [versions](alembic/versions) folder.
```shell
alembic upgrade <Revision-ID>
```

Running downgrade.
```shell
alembic downgrade -1
```

## Testing

### Why `lifespan` instead of top-level `create_all`

`models.Base.metadata.create_all(bind=engine)` at the top level of `main.py` runs at **import time**.
This means the moment a test imports `app`, it tries to connect to PostgreSQL — even if the test uses SQLite.
Moving it into the `lifespan` function ensures it only runs when the app actually starts, so tests can override the DB before any connection is made.

## pytest
```shell
pytest
```

Disabling warnings
```shell
pytest --disable-warnings
```

 To see prints, run with the `-s `flag: 
 ```shell
pytest -s
```