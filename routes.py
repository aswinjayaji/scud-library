from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_book,
    delete_book,
    retrieve_book,
    retrieve_books,
    update_book,
)
from models import (
    ErrorResponseModel,
    ResponseModel,
    BookModel,
    UpdateBookModel,
)

router = APIRouter()