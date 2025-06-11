from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter()

@router.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(database.get_db)):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

@router.get("/appointments/", response_model=list[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

