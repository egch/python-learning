import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool, text
from sqlalchemy.orm import sessionmaker

from src.database import Base
from src.main import app
from src.models import Todos

SQLALCHEMY_DATABASE_URL = 'sqlite:///./testdb.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'enrico', 'id': 1, 'user_role': 'admin'}

client = TestClient(app)


@pytest.fixture()
def test_todo():
    # --- SETUP (runs before the test) ---
    todo = Todos(
        title="Learning to code",
        description="Need to learn every day",
        priority=5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo  # <-- hands the todo to the test, pauses here
    # --- TEARDOWN (runs after the test) ---
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))  # cleans up the DB
        connection.commit()
