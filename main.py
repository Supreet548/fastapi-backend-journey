from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Student(BaseModel):
    name:str
    marks:int



@app.get("/")
def home():
    return {"message": "Hello AI Engineer"}

@app.get("/about")
def about():
    return {"message": "Learning FastAPI"}


@app.get("/student/{student_id}")
def get_student(student_id:int):
    return {"student_id":student_id}

@app.get("/search")
def search(name:str):
    return{"student_name":name}

@app.post("/students")
def create_student(student:Student):
    return{
        "message":"Student created",
        "student": student

    }