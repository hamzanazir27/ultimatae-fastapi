from fastapi import FastAPI
from . import models
from .database import engine
from .routers import todos, auth,admin,users


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}