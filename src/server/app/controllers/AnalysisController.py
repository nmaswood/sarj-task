from app.services import AnalysisService
from app.schemas.AnalysisSchema import AnalysisResponse

async def analyze_characters(book_id: str) -> AnalysisResponse:
    try:
        return await AnalysisService.analyze_characters(book_id)
    except Exception as e:
        raise

async def detect_language(book_id: str) -> AnalysisResponse:
    try:
        return await AnalysisService.detect_language(book_id)
    except Exception as e:
        raise

async def analyze_sentiment(book_id: str) -> AnalysisResponse:
    try:
        return await AnalysisService.analyze_sentiment(book_id)
    except Exception as e:
        raise

async def generate_summary(book_id: str) -> AnalysisResponse:
    try:
        return await AnalysisService.generate_summary(book_id)
    except Exception as e:
        raise
