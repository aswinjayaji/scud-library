from typing import Optional
from pydantic import BaseModel ,EmailStr,Field,validator
from datetime import datetime
from bson.objectid import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class BookModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title:str = Field(...)
    subtitle:str =Field(...)
    author:str =Field(...) 
    isbn:int =Field(...)
    price:int =Field(...)
    borrowerid:str =None
    # publication_date:datetime =Field(...)
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example":{
                "title":"The Da Vinci Code",
                "subtitle":"vol 1",
                "author":"Dan Brown",
                "isbn":9780385504201,
                "price":500,
                "borrowerid":None
            }
        }

class UpdateBookModel(BaseModel):
    title:Optional[str] 
    subtitle:Optional[str] 
    author:Optional[str]  
    isbn:Optional[int] 
    price:Optional[int] 
    borrowerid:Optional[str] 
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example":{
                "title":"The Da Vinci Code",
                "subtitle":"vol 1",
                "author":"Dan Brown",
                "isbn":9780385504201,
                "price":450,
                "borrowerid":None
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

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username:str=Field(...)
    name:str=Field(...)
    admin:bool =Field(default_factory=False)
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example":{
               "username":"johndoe",
               "name":"John Doe",
               "admin":False
            }
        }