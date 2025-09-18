from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel
from todoapp.models import Users
from passlib.context import CryptContext
from todoapp.database import SessionLocal
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

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

# helper functions
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True




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



@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
       return "Failed Authentication"
    return "Successful Authentication"

