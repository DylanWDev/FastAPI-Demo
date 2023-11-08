from fastapi import FastAPI
from models import Hero, Ability, AbilityType, Relationship, RelationshipType
from sqlalchemy import select
from enum import Enum

from routes import heroes

app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def read_root():
    return {"msg": "hello world"}