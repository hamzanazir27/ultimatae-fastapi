from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel
from todoapp.models import Users
from passlib.context import CryptContext
from todoapp.database import SessionLocal
from starlette import status

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]



class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/")
async def get_user():
    return {"user": "authenticated"}


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    role=create_user_request.role,
    hashed_password = bcrypt_context.hash(create_user_request.password),
    is_active=True)

    db.add(create_user_model)
    db.commit()

    return create_user_model

