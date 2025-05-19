import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('user')}:{os.getenv('password')}@{os.getenv('host')}/{os.getenv('database')}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False