from fastapi import FastAPI

from src import models
from src.database import engine
from src.routers import auth, todos, admin

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
