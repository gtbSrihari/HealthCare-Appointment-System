from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas

WORK_START = 9
WORK_END = 17

def add_doctor(db: Session, doctor: schemas.DoctorCreate):
    new_doc = models.Doctor(
        name=doctor.name,
        specialty=doctor.specialty,
        available_slots=doctor.available_slots
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc


def get_doctors(db: Session):
    return db.query(models.Doctor).all()


def get_doctor_by_id(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


def book_appointment(db: Session, doctor_id: int, appt: schemas.AppointmentCreate):
    doctor = get_doctor_by_id(db, doctor_id)
    if not doctor:
        raise ValueError("Doctor not found")

    # Validate working hours
    try:
        hour = int(appt.time_slot.split(":")[0])
    except:
        raise ValueError("Invalid time format, use HH:MM")

    if hour < WORK_START or hour >= WORK_END:
        raise ValueError("Appointment must be between 9 AM and 5 PM")

    # Check slot availability
    if doctor.available_slots <= 0:
        raise ValueError("No available slots")

    new_appt = models.Appointment(
        doctor_id=doctor_id,
        patient_name=appt.patient_name,
        appointment_date=appt.appointment_date,
        time_slot=appt.time_slot
    )

    doctor.available_slots -= 1
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)
    return new_appt


def cancel_appointment(db: Session, appointment_id: int):
    appt = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appt:
        raise ValueError("Appointment not found")
    if appt.is_canceled:
        raise ValueError("Appointment already canceled")

    appt.is_canceled = True
    doctor = appt.doctor
    doctor.available_slots += 1
    db.commit()
    db.refresh(appt)
    return appt
