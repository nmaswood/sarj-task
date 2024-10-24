import os
import logging
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI
from app.routes import health, books, analysis
from config.config import Config
from alembic.config import Config as AlembicConfig
from alembic import command
from limits.aio.storage import MemoryStorage
from limits.aio.strategies import FixedWindowRateLimiter
from fastapi.middleware.cors import CORSMiddleware
from fastlimits import RateLimitingMiddleware, limit


# Setup FastAPI app with title
app = FastAPI(title="Project Gutenberg Analysis API", debug=True)

# Setup logging
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

logger.info('App startup')

# Add the global rate limiting middleware
limiter = FixedWindowRateLimiter(storage=MemoryStorage())


# Add Cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://sarj-task-client.onrender.com'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=[
        "Content-Type",
        "Authorization",
        "Accept",
        "Accept-Language",
        "Accept-Encoding",
    ],
)

# Add Rate Limit Middleware
app.add_middleware(
    RateLimitingMiddleware,
    strategy=limiter,
)

@app.on_event("startup")
async def startup_event():
    # Any startup logic like initializing the database connection can go here
    print(f"App started successfully")

    alembic_cfg = AlembicConfig("alembic.ini")
    command.upgrade(alembic_cfg, "head")

# Include Routers
app.include_router(health.router, prefix="/api/health")
app.include_router(books.router, prefix="/api/v1")
app.include_router(analysis.router, prefix="/api/v1")


limit(app, "15/minute")
__all__ = ["app"]

from app import app
