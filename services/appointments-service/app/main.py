from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.database import SessionLocal

app = FastAPI()

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/appointments")
def read_appointments(db: Session = Depends(get_db)):
    # Usa `db` para interactuar con la base de datos
    return {"message": "funciona"}


##DATABASE_URL = "mysql+pymysql://user:password@db_host:3306/appointments_db"
##
##engine = create_engine(DATABASE_URL)
##SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
##
##Base = declarative_base()
##
##class Appointment(Base):
##    __tablename__ = "appointments"
##    id = Column(Integer, primary_key=True, index=True)
##    pet_name = Column(String(255), nullable=False)
##    owner_name = Column(String(255), nullable=False)
##    date = Column(DateTime, nullable=False)
##    reason = Column(String(255), nullable=True)
##
##Base.metadata.create_all(bind=engine)
##
##class AppointmentCreate(BaseModel):
##    pet_name: str
##    owner_name: str
##    date: datetime
##    reason: str | None = None
##
##@app.post("/appointments")
##def create_appointment(appointment: AppointmentCreate):
##    db = SessionLocal()
##    db_appointment = Appointment(
##        pet_name=appointment.pet_name,
##        owner_name=appointment.owner_name,
##        date=appointment.date,
##        reason=appointment.reason
##    )
##    db.add(db_appointment)
##    db.commit()
##    db.refresh(db_appointment)
##    db.close()
##    return {"message": "Cita creada", "id": db_appointment.id}
