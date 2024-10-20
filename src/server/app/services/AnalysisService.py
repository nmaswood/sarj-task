from app.services import BookService
from app.utils.llm import analyze_with_llm
from textblob import TextBlob
from langdetect import detect

async def analyze_characters(book_id: int):
    book = await BookService.get_book(book_id)
    return await analyze_with_llm(book.content, "Identify key characters in this text")

async def detect_language(book_id: int):
    book = await BookService.get_book(book_id)
    return detect(book.content)

async def analyze_sentiment(book_id: int):
    book = await BookService.get_book(book_id)
    blob = TextBlob(book.content)
    return {"sentiment": blob.sentiment.polarity}

async def generate_summary(book_id: int):
    book = await BookService.get_book(book_id)
    return await analyze_with_llm(book.content, "Generate a plot summary for this book")
