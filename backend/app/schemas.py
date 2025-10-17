from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class DoctorBase(BaseModel):
    name: str
    specialty: str
    available_slots: int = Field(gt=0, description="Must be a positive number")

class DoctorCreate(DoctorBase):
    pass

class DoctorResponse(DoctorBase):
    id: int
    class Config:
        orm_mode = True


class AppointmentBase(BaseModel):
    patient_name: str
    appointment_date: date
    time_slot: str

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int
    doctor_id: int
    is_canceled: bool
    class Config:
        orm_mode = True
