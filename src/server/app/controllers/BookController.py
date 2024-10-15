from app.services import BookService
from app.schemas import BookSchema, SuccessResponse

async def get_book(book_id: str):
    try:
        return await BookService.get_book(book_id)
    except Exception as e:
        raise
        

async def save_book(book: BookSchema):
    try:
        await BookService.save_book(book)
        return SuccessResponse(message="Book saved successfully")
    except Exception as e:
        raise

async def get_saved_books():
    try:
        return await BookService.get_saved_books()
    except Exception as e:
        raise
