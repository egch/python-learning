from fastapi import APIRouter
from pydantic import BaseModel

from models import Users

router = APIRouter()

class CreateUserRequest(BaseModel):

    email: str
    username:  str
    firstName: str
    lastName: str
    password: str
    role: str



@router.post("/auth/")
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username= create_user_request.username,
        firstName=create_user_request.firstName,
        lastName=create_user_request.lastName,
        role= create_user_request.role,
        hashed_password= create_user_request.password,
        is_active = True
    )
    return create_user_model
