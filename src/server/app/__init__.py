from fastapi import FastAPI
from app.routes import books
from config.config import Config  # Import the configuration

app = FastAPI(title="Project Gutenberg Analysis API")

@app.on_event("startup")
async def startup_event():
  # Any startup logic like initializing the database connection can go here
  print(f"Using database: {Config.SQLALCHEMY_DATABASE_URI}")
  print(f"Supported languages: {Config.LANGUAGES}")

# Include Routers
app.include_router(books.router, prefix="/api/v1")

# Health check endpoint
@app.get("/api/health")
async def health_check():
  return {"status": "healthy"}
