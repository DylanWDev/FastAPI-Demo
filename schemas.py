from types import Optional

from pydantic import BaseModel

# create these pydantic models (schemas)
# Hero, Ability, AbilityType, Relationship, RelationshipType

# Data Model
class HeroModel(BaseModel):
    id: int
    name: str | None
    about_me: str | None
    biography: str | None
    image_url: str | None

    def __init__(self, **data):
        super().__init__(**data)

        class Config:
            from_attributes = True