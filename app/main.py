from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

from security import verify_password, create_access_token

from fastapi import HTTPException
from security import oauth2_scheme, verify_token

from routers import students
from routers import auth

app = FastAPI()

app.include_router(students.router)

app.include_router(auth.router)

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



@app.post("/login")
def login(
    user:schemas.LoginRequest,
    db:Session=Depends(get_db)
):
    db_user = crud.get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        return {"error":"Invalid email"}
    
    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        return {"error":"Invalid password"}
    

    access_token = create_access_token(
        data = {"sub":db_user.email}
    )


    return {
        "access_token":access_token,
        "token_type":"bearer"
    }


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    email = verify_token(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = crud.get_user_by_email(
        db,
        email
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


@app.get("/me")
def read_current_user(
    token: str,
    db: Session = Depends(get_db)
):

    email = verify_token(token)

    return {"email": email}

@app.post("/notes")
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return crud.create_note(
        db,
        note,
        current_user.id
    )