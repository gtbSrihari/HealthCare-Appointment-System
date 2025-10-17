from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book/{doctor_id}", response_model=schemas.AppointmentResponse)
def book(doctor_id: int, appt: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    try:
        return crud.book_appointment(db, doctor_id, appt)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/cancel/{appointment_id}")
def cancel(appointment_id: int, db: Session = Depends(get_db)):
    try:
        appt = crud.cancel_appointment(db, appointment_id)
        return {"message": f"Appointment {appointment_id} canceled successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
