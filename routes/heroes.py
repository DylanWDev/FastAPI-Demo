from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
import schemas

router = APIRouter(
    prefix="/heroes"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.HeroModel])
def get_heroes(db: Session = Depends(get_db)):
    #get crud oporation to return the list of Heroes
    heroes = None
    return heroes
