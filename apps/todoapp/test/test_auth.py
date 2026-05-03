from calendar import isleap
from uu import encode

from starlette import status

from .utils import *
from src.routers.auth import get_db, authenticate_user, create_access_token, SECRET_KEY, ALGORITHM,get_current_user
from jose import jwt
from datetime import timedelta
import pytest

from fastapi import HTTPException
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

# I need this annotation when testing async methods
@pytest.mark.asyncio
# I am testing an async function, so I need async (?)
async def test_get_current_user_valid_token():
    encode = {'sub': 'testuser', 'id':1, 'role': 'admin'}
    # keyword args can be in any order as long as the argument name is specified
    token = jwt.encode(encode, key=SECRET_KEY, algorithm=ALGORITHM)
    user = await get_current_user(token=token)
    assert user == {'username': 'testuser', 'id': 1, 'user_role': 'admin'}

@pytest.mark.asyncio
# I am testing an async function, so I need async (?)
async def test_get_current_user_missing_payload():
    encode = {'role': 'user'}
    token = jwt.encode(encode, key=SECRET_KEY, algorithm=ALGORITHM)

    """
    pytest.raises is a context manager that catches an expected exception.
    It's saying: "run this code and expect it to raise an HTTPException".
    If no exception is raised, the test fails. excInfo holds the caught exception so you can inspect it.
    """
    with pytest.raises(HTTPException) as excInfo:
        await get_current_user(token=token)
    assert excInfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excInfo.value.detail == 'Could not validate user.'



