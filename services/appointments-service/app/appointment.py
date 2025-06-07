from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AppointmentOut)
def create_appointment(app: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    db_app = models.Appointment(**app.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app
