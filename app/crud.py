from sqlalchemy.orm import Session
from security import hash_password
import models
import schemas

#Create Student
def create_student(db:Session, student:schemas.StudentCreate):
    db_student= models.Student(
        name = student.name,
        marks = student.marks

    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student

#Read all students
def get_students(db:Session):
    return db.query(models.Student).all()

#Get Single student
def get_student(db:Session,student_id:int):

    return db.query(models.Student).filter(
        models.Student.id==student_id
    ).first()

def get_student_by_name(db:Session,name:str):
    return db.query(models.Student).filter(
        models.Student.name==name
    ).first()

#Update

def update_student(db:Session, student_id:int, updated_student: schemas.StudentCreate):
    student = db.query(models.Student).filter(
        models.Student.id==student_id
    ).first()

    if not student:
        return None
    
    student.name = updated_student.name 
    student.marks = updated_student.marks

    db.commit()
    db.refresh(student)

    return student

#Delete student
def delete_student(db:Session, student_id:int):
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if not student:
        return None
    

    db.delete(student)
    db.commit()

    return student 


def create_user(
        db: Session,
        user: schemas.UserCreate
):
    hashed_pw = hash_password(user.password)

    db_user = models.User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_pw
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def create_note(
        db:Session,
        note:schemas.NoteCreate
):
    db_note=models.Note(
        title=note.title,
        content=note.content,
        user_id=note.user_id
    )
    
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

def get_user_notes(
        db:Session,
        user_id:int
):
    return db.query(models.Note).filter(
        models.Note.user_id==user_id
    ).all()

    