from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class Role(str, Enum):
    owner = "owner"
    doctor = "doctor"
    admin = "admin"

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[Role] = None

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    role: Role

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=50)

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

