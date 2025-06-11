from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    pet_name: str
    owner_name: str
    date: datetime
    reason: str | None = None

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
