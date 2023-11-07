from typing import List
from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

from database import Base



class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    about_me = Column(String)
    biography = Column(String)
    image_url = Column(String)

    abillities: Mapped[List["Ability"]] = relationship(
        back_populates="hero", cascade = "all, delete-orphan")
    
    relationship: Mapped[List["Ability"]] = relationship(
        back_populates="hero", cascade = "all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"Hero(id={self.id!r}), name={self.name!r}, about_me={self.about_me!r}, biography={self.biography!r}, image_url={self.image_url!r})"
    


class Ability(Base):
    __tablename__ = "abilities"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    ability_type_id: Mapped[int] = mapped_column(ForeignKey("ability_types.id"))
    hero_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))

    hero: Mapped["Hero"] = relationship(back_populates="abilities")

    def __repr__(self) -> str:
        return f"ability(id={self.id!r}, ability_type_id={self.ability_type_id!r}, hero_id={self.hero_id!r})"
    


class Relationship(Base):
    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hero1_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))
    hero2_id: Mapped[int] = mapped_column(ForeignKey("heroes.id"))
    relationship_type_id: Mapped[int] = mapped_column(ForeignKey("relationship_type_id"))

    hero1: Mapped["Hero"] = relationship(back_populates="relationship")
    hero2: Mapped["Hero"] = relationship(back_populates="relationship")
    def __repr__(self) -> str:
        return f"Relationship(id={self.id!r}, hero1_id={self.id!r}, hero2_id{self.hero2_id!r}, relationship_type_id={self.relationship_type_id!r})"



class AbilityType(Base):
    __tablename__ = "ability_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"AbilityType(id={self.id!r}, name={self.name!r})"
    


class RelationshipType(Base):
    __tablename__ = "relationship_types"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"AbilityType(id={self.id!r}, name={self.name!r})"