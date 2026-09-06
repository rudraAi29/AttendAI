from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import SessionLocal, Student
import os

app = FastAPI(title="ATTEND AI API - Smart Attendance")

# Setup API Key Security
API_KEY = os.getenv("API_KEY", "admin_2026")
api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Access denied: Invalid API Key")
    return api_key

class CheckInRequest(BaseModel):
    name: str
    status: str = "Present"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Class Attendance System"}

@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# Added API Key dependency to the POST route
@app.post("/check_in/")
def check_in_student(request: CheckInRequest, db: Session = Depends(get_db), key: str = Depends(verify_api_key)):
    student = db.query(Student).filter(Student.name == request.name).first()
    
    try:
        if student:
            student.status = request.status
            db.commit()
            db.refresh(student)
            return {"message": f"Updated {request.name}'s status to {request.status}"}
        else:
            new_student = Student(name=request.name, status=request.status)
            db.add(new_student)
            db.commit()
            db.refresh(new_student)
            return {"message": f"Registered new student {request.name} as {request.status}"}
            
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred.")
