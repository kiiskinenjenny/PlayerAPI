from fastapi import FastAPI
from .routers import events, player

from .database import models
from .database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(player.router)
app.include_router(events.router)