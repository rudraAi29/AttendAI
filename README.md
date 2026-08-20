# 🚀 AttendAI: Real-Time Smart Attendance System

AttendAI is a full-stack, distributed computer vision and attendance tracking application. It is designed to capture student check-ins via a remote webcam client, process them through a secure backend API, and display live updates on an interactive real-time dashboard.

---

## 🛠️ Tech Stack & Architecture

* **Backend API:** FastAPI, Uvicorn (Asynchronous Python Server)
* **Database & ORM:** SQLite, SQLAlchemy
* **Computer Vision & Client:** OpenCV (`cv2`), Python Requests
* **Frontend Dashboard:** Streamlit (Real-time web interface)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
AttendAI_Backend/
│
├── main.py            # FastAPI backend endpoints & server logic
├── models.py          # SQLAlchemy database models & setup
├── app.py             # Streamlit real-time frontend dashboard
├── webcam_client.py   # OpenCV client script for remote video capture
├── requirements.txt   # Project dependencies
└── .gitignore         # Excludes venv, database, and cache files