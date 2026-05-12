from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name : str
    marks : int


#CREATE

@app.post("/students")
def create_students(student:Student):
    students.append(student.model_dump())
    return{
        "message":"Student added",
        "students":students
    }

#READ

@app.get("/students")
def get_students():
    return students

#UPDATE

@app.put("/students/{student_id}")
def update_student(student_id:int, updated_student:Student):
    if student_id>=len(students):
        return{"error":"Student not found"}
    
    students[student_id]=updated_student.model_dump()

    return{
        "message":"Student updated",
        "students":students
    }

#DELETE

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    if student_id>=len(students):
        return{"error":"Student not found"}
    
    deleted_student = students.pop(student_id)

    return{
        "message":"Student deleted",
        "students":deleted_student
    }