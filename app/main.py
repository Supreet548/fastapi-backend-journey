from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

app = FastAPI()

#create  tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()


    try:
        yield db

    finally:
        db.close()



@app.post("/students")
def create_student(
    student: schemas.StudentCreate,
    db:Session= Depends(get_db)
):
    
    return crud.create_student(
        db=db,
        student=student
    )


#GET all

@app.get("/students", response_model=list[schemas.StudentResponse])
def get_student(db:Session=Depends(get_db)):

    return crud.get_students(db)

#search

@app.get("/students/search/")
def search_student(
    name : str,
    db: Session= Depends(get_db)
):
    return crud.get_student_by_name(db,name)


#Get Single
@app.get("/student/{student_id}",response_model=schemas.StudentResponse)
def get_student(
    student_id:int,
    db: Session = Depends(get_db)
):
    return crud.get_student(db,student_id)


#UPDATE
@app.put(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
)
def update_student(
    student_id:int,
    updated_student: schemas.StudentCreate,
    db: Session= Depends(get_db)
):
    return crud.update_student(
        db,
        student_id,
        updated_student
    )


#DELETE
@app.delete(
    "/students/{student_id}",
    response_model=schemas.StudentResponse
    
)

def delete_student(
    student_id: int,
    db:Session=Depends(get_db)
):
    return crud.delete_student(db,student_id)



@app.post("/register", response_model=schemas.UserResponse)
def register_user(
    user:schemas.UserCreate,
    db:Session=Depends(get_db)
):
    return crud.create_user(db,user)



@app.post(
    "/notes",
    response_model=schemas.NoteResponse

)
def create_note(
    note:schemas.NoteCreate,
    db: Session= Depends(get_db)

):
    return crud.create_note(db,note)


@app.get(
    "/users/{user_id}/notes",
    response_model=list[schemas.NoteResponse]
)

def get_user_notes(
    user_id:int,
    db: Session= Depends(get_db)
):
    return crud.get_user_notes(db,user_id)