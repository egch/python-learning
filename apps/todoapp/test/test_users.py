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


def test_change_password_success(test_user):
    response = client.put('/user/password', json={"password":"testpassword",
                                                  "new_password": "xxxxxxxxxxxx"})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put('/user/password', json={"password":"wrong-pwd",
                                                  "new_password": "xxxxxxxxxxxx"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail" : "Error on password change"}


def test_change_phone_number(test_user):
    response = client.put('/user/phonenumber/222')
    assert response.status_code == status.HTTP_204_NO_CONTENT
