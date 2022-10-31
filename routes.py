from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_book,
    delete_book,
    retrieve_book,
    retrieve_books,
    update_book,
    retrieve_user,
    user_details,
    book_collection
)
from models import (
    ErrorResponseModel,
    ResponseModel,
    BookModel,
    UpdateBookModel,
    User
)

router = APIRouter()

@router.post("/add", response_description="book added into the database")
async def add_books(book_data:BookModel=Body(...)):
       book = jsonable_encoder(book_data)
       new_book = await book_collection.insert_one(book)
       created_book = await book_collection.find_one({"_id":new_book.inserted_id})
       return ResponseModel(created_book , "book created")

@router.get("/books",response_description="Books that are in the database")
async def get_books():
    book = await retrieve_books()
    if book:
        return ResponseModel(book, "Books ")
    return ResponseModel(book,"Empty List Returned")
        
@router.post("/user", response_description="user added into the database")
async def add_users(user_data:User=Body(...)):
       user = jsonable_encoder(user_data)
       new_user = await user_details.insert_one(user)
       created_user = await user_details.find_one({"_id":new_user.inserted_id})
       return ResponseModel(created_user , "user created")
   
@router.get("/users",response_description="Users retrieved")
async def get_user():
    user = await retrieve_user()
    if user:
        return ResponseModel(user, "Users ")
    return ResponseModel(user,"Empty List Returned")