# app/routes/analysis_routes.py
from fastapi import APIRouter
from app.controllers import analysis_controller

router = APIRouter()

@router.post("/characters")
async def analyze_characters(book_id: int):
    return await analysis_controller.analyze_characters(book_id)

@router.post("/language")
async def detect_language(book_id: int):
    return await analysis_controller.detect_language(book_id)

@router.post("/sentiment")
async def analyze_sentiment(book_id: int):
    return await analysis_controller.analyze_sentiment(book_id)

@router.post("/summary")
async def generate_summary(book_id: int):
    return await analysis_controller.generate_summary(book_id)
