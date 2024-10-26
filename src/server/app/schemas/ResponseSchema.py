from app.models.base import PydanticBaseModel
from typing import Optional

class SuccessResponse(PydanticBaseModel):
    message: Optional[str]
    status: str="success"
    

class ErrorResponse(PydanticBaseModel):
    message: Optional[str]
    status: str="error"
