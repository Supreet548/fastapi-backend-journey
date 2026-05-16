from database import Base
from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    marks = Column(Integer)


class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    notes = relationship("Note", back_populates="owner")

    


class Note(Base):
    __tablename__="notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    user_id=Column(
        Integer,
        ForeignKey("users.id")
        )

    owner = relationship("User", back_populates="notes")



