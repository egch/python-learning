from fastapi import status

from src.routers.admin import get_current_user, get_db
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


###############################################
# Test
###############################################

def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "title": "Learning to code",
            "description": "Need to learn every day",
            "priority": 5,
            "complete": False,
            "owner_id": 1,
            "id": 1
        }
    ]

def test_delete_todo(test_todo):
    response = client.delete("/admin/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    list = db.query(Todos).filter(Todos.id == 1).all()
    assert not list

def test_delete_todo_not_found():
    response = client.delete("/admin/todo/1")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo not found"}