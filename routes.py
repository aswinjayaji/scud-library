from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

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

@router.post("/addbook/{id}", response_description="book added into the database")
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

@router.get("/searchbook/{name}", response_description="Student data retrieved")
async def get_book(name):
    book = await retrieve_book(name)
    if book:
        return ResponseModel(book, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

@router.put("/bookupdate/{name}&{id}")
async def update_student_data(name:str,id: str, req: UpdateBookModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    user = await user_details.find_one({"_id":id})
    if user and user["admin"]:
        updated_book = await update_book(name, req)
        if updated_book:
            return ResponseModel(
                "Book with ID: {} name update is successful".format(id),
                "Book name updated successfully",
            )
        return ErrorResponseModel(
            "An error occurred",
            404,
            "There was an error updating the Book data.",
        )
    return ErrorResponseModel(
            "An error occurred",
            404,
            "user doesnot have permission to delete data",
        )
@router.put("/bookreturn/{name}&{user}")
async def borrow_book_data(name: str,user:str):
    book = await book_collection.find_one({"title": name})
    user = await user_details.find_one({"name": user})
    print(book)
    # print(updated_book,req)
    if book and book["borrowerid"] == user["_id"]:
        updated_book = await book_collection.update_one(
            {"_id": book["_id"]}, {"$set": {'borrowerid':None}}
        )
        print(updated_book)
        book=await book_collection.find_one({"_id": book["_id"]})
        return ResponseModel(book, "returned successfully")
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )
@router.put("/bookborrow/{name}&{user}")
async def borrow_book_data(name: str,user:str):
    book = await book_collection.find_one({"title": name})
    user = await user_details.find_one({"name": user})
    # print(book)
    # print(updated_book,req)
    if book:
        updated_book = await book_collection.update_one(
            {"_id": book["_id"]}, {"$set": {'borrowerid':user["_id"]}}
        )
        book = await book_collection.find_one({"_id": book["_id"]})
        return ResponseModel(book, "borrowered by {} successfully".format(user["name"]))
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )

@router.delete("/{name}&{id}", response_description="Student data deleted from the database")
async def delete_book_data(name: str ,id:str):
    user = await user_details.find_one({"_id":id})
    
    if user and user["admin"]:
      deleted_book= await delete_book(name)
      if deleted_book :
        return ResponseModel(
            "Book with name: {} removed by {}".format(name,user["name"]), "Book deleted successfully"
        )
        return ErrorResponseModel(
        "An error occurred", 404, "Book with id {0} doesn't exist".format(id)
        )
    return ErrorResponseModel(
        "An error occurred", 404, "User doesn't have permission to delete"
    )