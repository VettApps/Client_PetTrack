from pydantic import BaseModel
from datetime import date

class PetBase(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    owner: str
    vaccination_card: str
    birth_date: date

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: int
    class Config:
        orm_mode = True