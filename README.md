# 🚀 AttendAI: Secure Backend API for Smart Attendance

AttendAI is a robust, lightweight backend microservice designed to handle real-time student attendance tracking. Built with FastAPI and SQLAlchemy, this API processes incoming check-in requests, validates data, and securely logs attendance into a relational database using API Key authentication.

## 🛠️ Tech Stack & Architecture

* **Backend Framework:** FastAPI, Uvicorn (High-performance asynchronous server)
* **Database & ORM:** SQLite, SQLAlchemy
* **Data Validation:** Pydantic
* **Security:** Header-based API Key Authentication

## 📂 Project Structure

```text
AttendAI_Backend/
│
├── main.py            # FastAPI backend endpoints, security logic, and routing
├── models.py          # SQLAlchemy database schema and models
├── requirements.txt   # Project dependencies
└── .gitignore         # Excludes venv, database, and cache files
## ⚙️ Getting Started & Installation

If you would like to run or test this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rudraAi29/AttendAI.git](https://github.com/rudraAi29/AttendAI.git)
cd AttendAI
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
# On Windows (PowerShell): venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server (FastAPI):**
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the frontend dashboard (Streamlit):**
   ```bash
   streamlit run app.py
   ```
