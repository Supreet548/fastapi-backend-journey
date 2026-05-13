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