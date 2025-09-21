from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import Annotated
from sqlalchemy.orm import Session
from todoapp.models import Todo
from ..database import  SessionLocal
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter(
    prefix='/api/todos',
    tags=['todos']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create reusable dependency
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    completed: bool   
    priority: int = Field(gt=0, le=5)  # Add priority field

@router.get("/")
async def read_all(user: user_dependency, db: db_dependency):
    if user is None:
      raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(Todo).filter(Todo.owner_id == user.get('id')).all()





# @router.get("/todos", status_code=status.HTTP_200_OK)
# def read_todos(db: db_dependency):
#     todos = db.query(Todo).all()   
#     if not todos:                  
#         raise HTTPException(status_code=404, detail="No todos found")
#     return todos

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependency,db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
      raise HTTPException(status_code=401, detail="Authentication Failed")
    todo_model = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency,
                     todo_request: TodoRequest,
                     db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = Todo(
        title=todo_request.title,
        description=todo_request.description,
        complete=todo_request.completed,  # Note: mapping completed -> complete
        priority=todo_request.priority,
        owner_id=user.get('id')  # You'll want to get this from authentication later
    )
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)  
    return todo_model

@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependency,db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    if user is None:
      raise HTTPException(status_code=401, detail="Authentication Failed")



    todo_model = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.complete = todo_request.completed  
    todo_model.priority = todo_request.priority

    db.add(todo_model)
    db.commit()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=404,detail="Authenticated failed")
    todo_model = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo_model)
    db.commit()







