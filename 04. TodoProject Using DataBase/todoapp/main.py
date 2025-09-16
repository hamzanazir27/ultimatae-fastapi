from fastapi import FastAPI
from . import models
from .database import engine

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Todo App is running 🚀"}
