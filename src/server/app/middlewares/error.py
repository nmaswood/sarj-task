# app/middleware/error_middleware.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

class ErrorMiddleware:
    async def __call__(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as exc:
            return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
        except Exception as exc:
            return JSONResponse(status_code=500, content={"detail": "Internal server error"})
