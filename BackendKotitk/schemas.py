from modulefinder import Module

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class SAllBreeds(Base):
    name: str


class SAllCats(Base):
    color: str
    age: int
    description: str
    breed: SAllBreeds


class SCreateCat(Base):
    color: str
    age: int
    description: str
    breed: SAllBreeds


class SUpdateCat(BaseModel):
    color: str | None = None
    age: int | None = None
    description: str | None = None
    breed_id: int | None = None


class SDeleteCat(BaseModel):
    cat_id: int

