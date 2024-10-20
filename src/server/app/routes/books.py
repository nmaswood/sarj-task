from fastapi import APIRouter
from app.controllers import BookController
from app.schemas import BookSchema

router = APIRouter()

@router.get("/{book_id}")
async def get_book(book_id: int):
  return BookController.get_book(book_id)

@router.post("/")
async def save_book(book: BookSchema):
  return BookController.create_book(book)

@router.get("/")
async def get_books():
  return BookController.get_books()
