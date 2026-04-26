from .utils import *
from src.routers.auth import get_db, authenticate_user

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
