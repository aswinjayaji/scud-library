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

@router.post("/add/{id}", response_description="book added into the database")
async def add_books(id:str,book_data:BookModel=Body(...)):
       book = jsonable_encoder(book_data)
       user = await user_details.find_one({"_id": id})
       if user and user['admin']:
        new_book = await book_collection.insert_one(book)
        created_book = await book_collection.find_one({"_id":new_book.inserted_id})
        return ResponseModel(created_book , "book created")
       return ErrorResponseModel("not allowed","404","user is not admin")

@router.get("/books",response_description="Books that are in the database")
async def get_books():
    book = await retrieve_books()
    if book:
        return ResponseModel(book, "Books ")
    return ResponseModel(book,"Empty List Returned")

@router.get("/book/{name}", response_description="Student data retrieved")
async def get_book(name):
    book = await retrieve_book(name)
    if book:
        return ResponseModel(book, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

# @router.put("/book/{id}")
# async def update_book_data(id: str, req: UpdateBookModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_book = await update_book(id, req)
#     if updated_book:
#         return ResponseModel(
#             "Book with ID: {} name update is successful".format(id),
#             "Book name updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the student data.",
#     )