from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel
from todoapp.models import Users
from passlib.context import CryptContext
from todoapp.database import SessionLocal
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 1) Annotated -> Python ko batata hai ke variable ka type kya hai (yahan Session)
# 2) Depends(get_db) -> FastAPI ko bolta hai ke database session get_db() se inject karo
# 3) Matlab: jab bhi db_dependency use karoge, FastAPI tumhe ek database session dega
db_dependency = Annotated[Session, Depends(get_db)]


# Generate secret with: openssl rand -hex 32
SECRET_KEY = "your-long-secret-string-here"
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str



class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str   # <-- new field




# CryptContext ek class hai jo password hashing/verification ke liye use hoti hai
# schemes=["bcrypt"] -> passwords ko bcrypt algorithm se hash karega
# deprecated="auto" -> agar koi purani hashing scheme ho to usse outdated mark karega


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 👉 oauth2_bearer ek dependency hai jo har request se JWT token nikalne ka kaam karegi, aur FastAPI ko batayegi ke wo token kahan se aayega (yani /auth/token route se).

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")




# helper functions
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user  # Return user object, not True


# create token function
def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expire = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
  

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')

        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials'
            )
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )




@router.get("/")
async def get_user():
    return {"user": "authenticated"}


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    role=create_user_request.role,
    hashed_password = bcrypt_context.hash(create_user_request.password),
    is_active=True,
    phone_number=create_user_request.phone_number   # <-- new field
)

    db.add(create_user_model)
    db.commit()

    return create_user_model



@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials'
        )

    token = create_access_token(user.username, user.id, user.role,timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}








# @router.get("/me")
# async def read_current_user(current_user: Annotated[dict, Depends(get_current_user)]):
#     # get_current_user token decode karke user info return karega
#     return {"user": current_user}




# Go to Authorize in Swagger UI.

# Fill in:

# username → The username you registered/stored in your DB.

# password → The corresponding password.

# Leave client_id and client_secret empty (unless you explicitly set them up).

# Click Authorize → Swagger will call auth/token and fetch a JWT access token.

# Once authorized, Swagger automatically attaches the Authorization: Bearer <your_token> header to all protected endpoints
# Go to Authorize in Swagger UI.

# Fill in:

# username → The username you registered/stored in your DB.

# password → The corresponding password.

# Leave client_id and client_secret empty (unless you explicitly set them up).

# Click Authorize → Swagger will call auth/token and fetch a JWT access token.

# Once authorized, Swagger automatically attaches the Authorization: Bearer <your_token> header to all protected endpoints