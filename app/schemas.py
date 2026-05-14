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