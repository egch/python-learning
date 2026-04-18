from contextlib import asynccontextmanager

from fastapi import FastAPI

from .import models
from .database import engine
from .routers import auth, todos, admin, users

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield

@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
