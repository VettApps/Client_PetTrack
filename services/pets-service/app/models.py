from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    species = Column(String(50))
    breed = Column(String(50))
    age = Column(Integer)
    owner = Column(String(100))
    vaccination_card = Column(String(200))  # ruta o texto JSON
    birth_date = Column(Date)