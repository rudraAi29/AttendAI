from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import SessionLocal, Student

app = FastAPI(title="ATTEND AI API - Smart Attendance")

# Define the JSON body structure (Professional Data Validation)
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

# 1. View all students and their attendance status
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# 2. Smart Check-In (Using JSON Body and Error Handling)
@app.post("/check_in/")
def check_in_student(request: CheckInRequest, db: Session = Depends(get_db)):
    # Check if student already exists in database using the request body
    student = db.query(Student).filter(Student.name == request.name).first()

    try:
        if student:
            # If student exists, update their status
            student.status = request.status
            db.commit()
            db.refresh(student)
            return {"message": f"Updated {request.name}'s status to {request.status}"}
        else:
            # If student doesn't exist, create a new record
            new_student = Student(name=request.name, status=request.status)
            db.add(new_student)
            db.commit()
            db.refresh(new_student)
            return {"message": f"Registered new student {request.name} as {request.status}"}
            
    except Exception as e:
        # Rollback the transaction if something goes wrong to prevent database corruption
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error occurred.")
