from app.services import BookService

async def get_book(book_id: int):
    return await BookService.get_book(book_id)

async def get_saved_books():
    return await BookService.get_saved_books()

async def search_books(query: str):
    return await BookService.search_books(query)
