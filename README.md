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
## ⚙️ Getting Started & Installation

If you would like to run or test this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rudraAi29/AttendAI.git
   cd AttendAI_Backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server (FastAPI):**
   ```bash
   uvicorn main:app --host 0.0.0.0 --reload --port 8000
   ```

5. **Run the frontend dashboard (Streamlit):**
   ```bash
   streamlit run app.py
   ```