from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    marks:int


class StudentResponse(BaseModel):
    id: int
    name: str
    marks: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username:str
    email:str
    password:str


class UserResponse(BaseModel):
    id:int
    username:str
    email:str

    class Config:
        from_attributes = True


class NoteCreate(BaseModel):

    title:str
    content:str
    user_id:int

class NoteResponse(BaseModel):
    id:int
    title:str
    content:str
    user_id:int

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email:str
    password:str



class NoteCreate(BaseModel):

    title: str
    content: str