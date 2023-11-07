from fastapi import FastAPI
from models import Hero, Ability, AbilityType, Relationship, RelationshipType

app = FastAPI()

@app.get("/")
async def read_root():
    return "hello world"