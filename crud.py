from sqlalchemy.orm import Session, aliased
from models import Hero, Ability, AbilityType, Relationship, RelationshipType
from schemas import HeroModel

def get_heroes_v1(db: Session):
    #set variable to store the query info
    heroes_query = (
        db.query(Hero).all()
    )
    return heroes_query

def get_heroes(db: Session):
    #set variable to store the query info
    heroes_query = (
        db.query(Hero)
        .join(Hero.abilities)
        .all()
    )
    return heroes_query