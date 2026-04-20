from sqlite3 import complete_statement

from dns.rdtypes.util import priority_processing_order
from sqlalchemy.orm import sessionmaker


from sqlalchemy import create_engine, StaticPool, text

from src.main import app
from src.database import Base
from src.routers.todos import get_db, get_current_user
from fastapi.testclient import  TestClient
from fastapi import status
import pytest
from src.models import Todos
from test.test_example import default_employee

from test.test_main import client

SQLALCHEMY_DATABASE_URL='sqlite:///./testdb.db'

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
    return {'username': 'enrico', 'id':1, 'user_role': 'admin'}

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

@pytest.fixture()
def test_todo():
    # --- SETUP (runs before the test) ---
    todo = Todos(
        title = "Learning to code",
        description = "Need to learn every day",
        priority=5,
        complete=False,
        owner_id=1
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo   # <-- hands the todo to the test, pauses here
    # --- TEARDOWN (runs after the test) ---
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))   # cleans up the DB
        connection.commit()

###############################################
# Test
###############################################

def test_read_all_authenticated(test_todo):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
      "title": "Learning to code",
      "description": "Need to learn every day",
      "priority": 5,
      "complete": False,
      "owner_id": 1,
      "id": 1
  }]


def test_read_one_authenticated(test_todo):
    response = client.get("/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
      "title": "Learning to code",
      "description": "Need to learn every day",
      "priority": 5,
      "complete": False,
      "owner_id": 1,
      "id": 1
  }

def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todo/3")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}

def test_create_todo(test_todo):
    request_data = {
        'title' : '99 kg',
        'description' : 'I need to lose weight!',
        'priority' : 5,
        'complete' : False
    }
    response = client.post("/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id ==2).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')


def test_update_todo(test_todo):
    request_data = {
        'title' : '99 kg',
        'description' : 'I need to lose weight!',
        'priority' : 5,
        'complete' : False
    }
    response = client.put("/todo/1", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id ==1).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')


def test_update_todo_not_found(test_todo):
    request_data = {
        'title' : '99 kg',
        'description' : 'I need to lose weight!',
        'priority' : 5,
        'complete' : False
    }
    response = client.put("/todo/99", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}

def test_delete_todo(test_todo):
    response = client.delete("/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    list = db.query(Todos).filter(Todos.id == 1).all()
    assert not list


def test_delete_todo_not_found():
    response = client.delete("/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}
