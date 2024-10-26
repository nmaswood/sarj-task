import os
import uvicorn
from config.config import Config

basedir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    uvicorn.run("app:app", host=Config.HOST, port=Config.PORT, reload=True)
