from typing import Optional
from pydantic import BaseModel ,EmailStr,Field
from datetime import datetime

class BookModel(BaseModel):
    title:str = Field(...)
    subtitle:str =Field(...)
    author:str =Field(...) 
    isbn:int =Field(...)
    price:int =Field(...)
    borrowerid:str =None
    # publication_date:datetime =Field(...)
    class Config:
        schema_extra = {
            "example":{
                "title":"The Da Vinci Code",
                "subtitle":"vol 1",
                "author":"Dan Brown",
                "isbn":9780385504201,
                "price":500,
                "borrowedid":None
            }
        }

class UpdateBookModel(BaseModel):
    title:str =Optional[str] 
    subtitle:str =Optional[str] 
    author:str =Optional[str]  
    isbn:int =Optional[int] 
    price:int =Optional[int] 
    borrowerid:str =Optional[str] 
    class Config:
            schema_extra = {
            "example":{
                "title":"The Da Vinci Code",
                "subtitle":"vol 1",
                "author":"Dan Brown",
                "isbn":9780385504201,
                "price":450,
                "borrowedid":None
            }
        }
def ResponseModel(data,message):
    return{
        "data":[data],
        "code":200,
        "message":message,
    }
    
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
