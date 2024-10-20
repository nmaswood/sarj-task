import os
import uvicorn
from app import app
from config.config import Config

basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
  uvicorn.run(app, host=Config.HOST, port=Config.PORT, reload=True)
