# 🏥 Healthcare Appointment System

A full-stack Healthcare Appointment Booking web application that allows users to view doctors, book appointments, and cancel them easily. The system ensures time-slot validation (working hours only) and automatic slot management.

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup (FastAPI)](#-backend-setup-fastapi)
  - [Frontend Setup (React)](#-frontend-setup-react)
- [API Endpoints](#-api-endpoints)
- [Business Logic](#-business-logic)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

## 🧠 Project Overview

This project implements an appointment scheduling platform for healthcare management. It demonstrates clean API design, modular routing, CRUD operations, and seamless frontend–backend integration.

-   **Backend:** A robust REST API built with **FastAPI**.
-   **Database:** **SQLite** with **SQLAlchemy** for data storage and ORM.
-   **Frontend:** A modern, responsive interface built with **React**, **Vite**, and **Tailwind CSS**.

## ✨ Features

-   ✅ **Doctor Management**: Add new doctors, view a list of all available doctors, and track their available appointment slots.
-   ✅ **Appointment Booking**: Schedule appointments with a specific doctor, validated against their working hours (09:00 AM – 05:00 PM). A doctor's available slots automatically decrease upon successful booking.
-   ✅ **Appointment Cancellation**: Cancel an existing appointment, which automatically restores the available slot to the corresponding doctor.
-   ✅ **Dynamic Frontend**: The user interface displays available doctors, provides intuitive forms for booking and cancellation, and is fully responsive.

## 🧰 Tech Stack

| Layer      | Technology                                    |
| :--------- | :-------------------------------------------- |
| **Frontend** | React, Vite, Tailwind CSS                     |
| **Backend** | FastAPI, SQLAlchemy, Pydantic                 |
| **Database** | SQLite                                        |
| **Language** | Python 3.10+, JavaScript (ES6)                |

## 🧱 Project Structure
# Project Structure
```
healthcare-appointment-system/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   └── routes/
│   │       ├── doctors.py
│   │       └── appointments.py
│   ├── run_server.bat
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── DoctorCard.jsx
│   │   │   ├── BookingForm.jsx
│   │   │   ├── CancelAppointment.jsx
│   │   │   ├── DoctorList.jsx
│   │   │   └── Notification.jsx
│   │   ├── utils/
│   │   │   └── defaultUtils.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── tailwind.config.js
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

-   Python 3.10+
-   Node.js v20.19.0 or higher
-   npm (Node Package Manager)

### 🚀 Backend Setup (FastAPI)

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the backend server:**
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```
    The API will be live at `http://localhost:8000`. You can access the auto-generated documentation at `http://localhost:8000/docs`.

### 💻 Frontend Setup (React)

1.  **Open a new terminal** and navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  **Install the npm dependencies:**
    ```bash
    npm install
    ```

3.  **Run the frontend development server:**
    ```bash
    npm run dev
    ```
    The React application will be available at `http://localhost:5173`.

## 🔗 API Endpoints

| Method   | Endpoint                                   | Description                         |
| :------- | :----------------------------------------- | :---------------------------------- |
| `POST`   | `/doctors/`                                | Add a new doctor.                   |
| `GET`    | `/doctors/`                                | List all available doctors.         |
| `GET`    | `/doctors/{doctor_id}`                     | Get a specific doctor by their ID.  |
| `POST`   | `/appointments/book/{doctor_id}`           | Book an appointment for a doctor.   |
| `DELETE` | `/appointments/cancel/{appointment_id}`    | Cancel an existing appointment.     |

## 💡 Business Logic

-   **Working Hours**: Appointments can only be booked between **09:00 AM** and **05:00 PM**.
-   **Time Slot Validation**: The backend validates that all appointment times fall within the allowed hourly slots (e.g., 09:00, 10:00, ..., 16:00).
-   **Slot Management**: A doctor's available slot count is automatically managed. It decreases on booking and increases on cancellation.

## 🧩 Future Enhancements

-   [ ] **User Authentication**: Implement JWT-based authentication for secure user accounts.
-   [ ] **Admin Panel**: Create a dedicated dashboard for administrators to manage doctors and appointments.
-   [ ] **Role-Based Access**: Differentiate between patient and admin roles with different permissions.
-   [ ] **Notifications**: Add email or SMS reminders for upcoming appointments.

## 👨‍💻 Author

**Sri Hari Kande**
- Machine Learning Engineer | Full Stack Developer