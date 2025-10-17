from fastapi import FastAPI
from .database import Base, engine
from .routes import doctors, appointments

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Healthcare Appointment Booking API",
    description="FastAPI backend for healthcare appointment scheduling system.",
    version="1.0.0"
)

app.include_router(doctors.router)
app.include_router(appointments.router)
