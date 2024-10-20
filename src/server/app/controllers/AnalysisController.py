from app.services import AnalysisService

async def analyze_characters(book_id: int):
    return await AnalysisService.analyze_characters(book_id)

async def detect_language(book_id: int):
    return await AnalysisService.detect_language(book_id)

async def analyze_sentiment(book_id: int):
    return await AnalysisService.analyze_sentiment(book_id)

async def generate_summary(book_id: int):
    return await AnalysisService.generate_summary(book_id)
