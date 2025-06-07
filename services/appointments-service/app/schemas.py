from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    pet_name: str
    owner_name: str
    date: datetime
    reason: str | None = None

class Appointment(AppointmentCreate):
    id: int

    class Config:
        orm_mode = True
