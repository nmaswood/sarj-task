import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  HOST = os.environ.get("HOST", "127.0.0.1")
  PORT = int(os.environ.get("PORT", 8000))
  SECRET_KEY = os.environ.get('SECRET_KEY', 'qwerty')
  DB_HOST = os.environ.get('DB_HOST')
  DB_NAME = os.environ.get('DB_NAME')
  DB_USERNAME = os.environ.get('DB_USERNAME')
  DB_PASSWORD = os.environ.get('DB_PASSWORD')

  # Windows Authentication
  SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{DB_HOST}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server&encrypt=true&trust_server_certificate=yes"

  # Uncomment the below if using SQL Server Authentication instead of Windows Authentication
  # SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server&encrypt=true&trust_server_certificate=yes"
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  LANGUAGES = ['en-US', 'en-GB', 'en-CA', 'es']
