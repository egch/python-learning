from calendar import isleap

from .utils import *
from src.routers.auth import get_db, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM
from jose import jwt
from datetime import timedelta
"""                                                                                                                                                                                                  
The line below is only needed for fastapi test
The test test_authenticate_user does not need it                                                                                                                                                                                    
"""
#app.dependency_overrides[get_db] = override_get_db


def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    authenticated_user = authenticate_user(test_user.username, 'testpassword', db)
    assert authenticated_user is not None
    assert authenticated_user.username == 'testuser'

def test_authenticate_not_existing_user(test_user):
    db = TestingSessionLocal()
    not_existing_user = authenticate_user('wrong-user', 'testpassword', db)
    assert not_existing_user is False

def test_authenticate_wrong_password_user(test_user):
    db = TestingSessionLocal()
    wrong_passsword_user = authenticate_user(test_user.username,'wrong-pwd', db)
    assert wrong_passsword_user is False


def test_create_access_token():
    username = 'testuser'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)
    assert token is not None
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM, options={'verify_signature': False})
    assert decoded_token['sub'] == username
    assert decoded_token['id'] == user_id
    assert decoded_token['role'] == role

# I am testing an async function, so I need async (?)
async def test_get_current_user():
    print("TBC")

