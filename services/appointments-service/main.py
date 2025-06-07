from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

app = FastAPI()

DATABASE_URL = "mysql+pymysql://user:password@db_host:3306/appointments_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    pet_name = Column(String(255), nullable=False)
    owner_name = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
    reason = Column(String(255), nullable=True)

Base.metadata.create_all(bind=engine)

class AppointmentCreate(BaseModel):
    pet_name: str
    owner_name: str
    date: datetime
    reason: str | None = None

@app.post("/appointments")
def create_appointment(appointment: AppointmentCreate):
    db = SessionLocal()
    db_appointment = Appointment(
        pet_name=appointment.pet_name,
        owner_name=appointment.owner_name,
        date=appointment.date,
        reason=appointment.reason
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    db.close()
    return {"message": "Cita creada", "id": db_appointment.id}
