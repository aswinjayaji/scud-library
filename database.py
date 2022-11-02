from pymongo import MongoClient
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
import motor.motor_asyncio

load_dotenv()
MONGODB_URL= os.getenv('MONGODB_URL')


client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
#When the first I/O operation is made, both the database
#and collection will be created if they don't already exist.
db = client.books
book_collection = db.get_collection("book_collections")
db = client.users
user_details = db["user_details"]




#helpers

def book_helper(book:dict) -> dict:
    return {
        "id":str(book["_id"]),
        "title":book["title"],
        "subtitle":book["subtitle"],
        "author":book["author"],
        "isbn":book["isbn"],
        "price":book["price"],
        "borrowerid":book["borrowerid"]         
    }
def user_helper(user:dict) -> dict:
    return {
        "id":str(user["_id"]),
        "name":user["name"],
        "admin":bool(user["admin"])
    }
    
#Retrieve all books present in the database  
async def retrieve_user():
    users=[]
    async for user in user_details.find():
        users.append(user_helper(user))
    return users




# Retrieve all books present in the database
async def retrieve_books():
    books = []
    async for book in book_collection.find():
        books.append(book_helper(book))
    return books


# Add a new book into to the database
async def add_book(book_data: dict) -> dict:
    book = await book_collection.insert_one(book_data)
    new_book = await book_collection.find_one({"_id": book.inserted_id})
    return book_helper(new_book)


# Retrieve a book with a matching ID
async def retrieve_book(name: str) -> dict:
    book = await book_collection.find_one({"title": name})
    if book:
        return book_helper(book)


# Update a book with a matching ID
async def update_book(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        updated_book = await book_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_book:
            return True
        return False


# Delete a book from the database
async def delete_book(id: str):
    book = await book_collection.find_one({"_id": ObjectId(id)})
    if book:
        await book_collection.delete_one({"_id": ObjectId(id)})
        return True