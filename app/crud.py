from sqlalchemy.orm import Session
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