from database import Base
from sqlalchemy import Column, Integer, String 

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

