from fastapi import FastAPI,Request
from . import models
from .database import engine
from .routers import todos, auth,admin,users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


# Configure templates
templates = Jinja2Templates(directory="todoapp/templates")


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="todoapp/static"), name="static")

app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(users.router)

@app.get("/")
def test_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
