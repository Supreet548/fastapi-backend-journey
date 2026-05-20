from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas

from database import SessionLocal

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get(
    "/",
    response_model=list[schemas.StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):

    return crud.get_students(db)