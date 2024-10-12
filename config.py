import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://csv:12345@localhost:5432/code')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
