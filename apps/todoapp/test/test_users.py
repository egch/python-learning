from fastapi import status

from src.routers.users import get_db, get_current_user
from .utils import *


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_get_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['email'] == 'test@test.com'
    assert response.json()['username'] == 'testuser'
    assert response.json()['first_name'] == 'John'
    assert response.json()['last_name'] == 'Doe'
    assert response.json()['is_active'] == True
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'
