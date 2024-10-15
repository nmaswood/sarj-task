from app.models.base import PydanticBaseModel
from typing import Optional, List, Dict

class AnalysisResponse(PydanticBaseModel):
    success: bool
    data: Optional[Dict] = None

class CharacterAnalysis(PydanticBaseModel):
    characters: List[Dict[str, str]]

class LanguageAnalysis(PydanticBaseModel):
    language_code: str
    confidence: float

class SentimentAnalysis(PydanticBaseModel):
    sentiment: float
    classification: str

class BookSummary(PydanticBaseModel):
    summary: str
    word_count: int
