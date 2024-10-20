from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import Config

# Create engine using the database URI from the config
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
