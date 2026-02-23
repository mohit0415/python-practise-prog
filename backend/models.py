from pydantic import BaseModel


class Product(BaseModel):
    id : int
    name : str
    price : int
    qty :int

class ProductDTO(BaseModel):
    name : str
    price : int
    qty : int

class ProfessorDTO(BaseModel):
    name : int
    name: str
    age : int
    subject : str
    qual : str

class ResponseDTO(BaseModel):
    statusCode : int
    message : str
    resObj : object

class ProfessorResponseDTO(BaseModel):
    id : int
    name : int
    name: str
    age : int
    subject : str
    qual : str

    class Config:
        from_attributes = True

class DeptReq(BaseModel):
    dept : str

class ProfessorFoundBy(BaseModel):
    id : int
    name : str
    dept : str

    class Config:
        from_attributes = True