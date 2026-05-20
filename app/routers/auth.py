from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas

from database import SessionLocal

from security import (
    verify_password,
    create_access_token
)

router = APIRouter(
    tags=["Authentication"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/login")
def login(
    user: schemas.LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = crud.get_user_by_email(
        db,
        user.email
    )

    if not db_user:
        return {"error": "Invalid email"}

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        return {"error": "Invalid password"}

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    } 