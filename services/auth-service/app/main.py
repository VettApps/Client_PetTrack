from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.middleware.cors import CORSMiddleware

import enum
from passlib.hash import bcrypt
import os

# ------------------ Configuración ------------------
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@db:3306/vet_auth")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ------------------ Modelo Enum y SQLAlchemy ------------------
class RoleEnum(str, enum.Enum):
    owner = "owner"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    role = Column(Enum(RoleEnum), default=RoleEnum.owner, nullable=False)
    is_active = Column(Boolean, default=True)

# ------------------ Pydantic Schemas ------------------
class RegisterRequest(BaseModel):
    email: str
    password: str
    full_name: str | None = None

class LoginRequest(BaseModel):
    email: str
    password: str

# ------------------ App Init ------------------
app = FastAPI()

# ------------------ Base de datos ------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

# ------------------ Endpoints ------------------

@app.post("/register")
def register_user(user: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    new_user = User(
        email=user.email,
        hashed_password=bcrypt.hash(user.password),
        full_name=user.full_name,
        role="owner"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuario registrado", "user_id": new_user.id}

@app.post("/login")
def login_user(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not bcrypt.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Inicio de sesión exitoso", "user_id": user.id, "role": user.role}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # o ["*"] para pruebas
    allow_credentials=True,
    allow_methods=["*"],   # Esto acepta GET, POST, OPTIONS, etc.
    allow_headers=["*"],
)