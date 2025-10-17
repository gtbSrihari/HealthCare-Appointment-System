from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/doctors", tags=["Doctors"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.DoctorResponse)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.add_doctor(db, doctor)

@router.get("/", response_model=list[schemas.DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

@router.get("/{doctor_id}", response_model=schemas.DoctorResponse)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doc = crud.get_doctor_by_id(db, doctor_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doc
