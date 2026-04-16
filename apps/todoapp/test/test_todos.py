
from sqlalchemy.orm import sessionmaker


from sqlalchemy import create_engine, StaticPool

from src.main import app
from src.database import Base
from src.routers.todos import get_db, get_current_user
from fastapi.testclient import  TestClient
from fastapi import status

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


###############################################
# Test
###############################################

def test_read_all_authenticated():
    responses = client.get("/")
    assert responses.status_code == status.HTTP_200_OK
    assert responses.json() == []
