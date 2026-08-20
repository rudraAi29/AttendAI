from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SessionLocal, Student

app = FastAPI(title="ATTEND AI API - Smart Attendance")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Class Attendance System"}

# 1. View all students and their attendance status
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# 2. Smart Check-In (Handles both auto-detection and manual entry)
@app.post("/check_in/")
def check_in_student(name: str, status: str = "Present", db: Session = Depends(get_db)):
    # Check if student already exists in database
    student = db.query(Student).filter(Student.name == name).first()
    
    if student:
        # If student exists, update their status (e.g., mark Present)
        student.status = status
        db.commit()
        db.refresh(student)
        return {"message": f"Updated {name}'s status to {status}"}
    else:
        # If student doesn't exist, create a new record
        new_student = Student(name=name, status=status)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"message": f"Registered new student {name} as {status}"}