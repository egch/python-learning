from warnings import deprecated

from fastapi import APIRouter, Depends

from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Annotated

from starlette import status

from database import SessionLocal
from models import Users
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class CreateUserRequest(BaseModel):
    email: str
    username:  str
    firstName: str
    lastName: str
    password: str
    role: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/auth/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username= create_user_request.username,
        firstName=create_user_request.firstName,
        lastName=create_user_request.lastName,
        role= create_user_request.role,
        hashed_password= bcrypt_context.hash(create_user_request.password),
        is_active = True
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token():
    return 'token'