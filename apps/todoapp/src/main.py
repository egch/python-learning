from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from . import models
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="src/templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
