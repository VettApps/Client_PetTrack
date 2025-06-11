from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine

# Crear tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pets Service")

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pets/", response_model=schemas.Pet)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    db_pet = models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

@app.get("/pets/", response_model=list[schemas.Pet])
def read_pets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Pet).offset(skip).limit(limit).all()

@app.get("/pets/{pet_id}", response_model=schemas.Pet)
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).get(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@app.put("/pets/{pet_id}", response_model=schemas.Pet)
def update_pet(pet_id: int, pet_in: schemas.PetCreate, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).get(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    for key, value in pet_in.dict().items():
        setattr(pet, key, value)
    db.commit()
    db.refresh(pet)
    return pet

@app.delete("/pets/{pet_id}", status_code=204)
def delete_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).get(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    db.delete(pet)
    db.commit()