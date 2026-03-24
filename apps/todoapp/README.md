# Todos 
You need to have a pycharm project starting from this folder!

## Commands

Create the venv env
```shell
p3 -m pip install --upgrade pip
p3 -m venv fastapienv 
```

Activate
```shell
source fastapienv/bin/activate
```
Install the dependencies
```shell
pip install "fastapi[standard]"
pip install passlib
pip install bcrypt==4.0.1
pip install python-multipart
pip install "python-jose[cryptography]"
pip install sqlalchemy
pip install psycopg2-binary
```

### fastapi commands
```shell
uvicorn src.main:app --reload
```

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

rm -rf data  
docker compose up

**Example (Docker volume):**

docker compose down -v  
docker compose up

This forces PostgreSQL to initialize a **fresh database cluster with the new configuration**.

### PgAdmin
![pgAdmin.png](docs/images/pgAdmin.png)
## Links
[jwt io](http://www.jwt.io)

### Change Password
Use this so you remember it: `12345!`