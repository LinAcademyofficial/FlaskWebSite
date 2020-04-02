import os


class Config:
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    MONGODB_PORT = os.getenv('MONGODB_PORT')
    SECRET_KEY = os.getenv('SECRET_KEY')


class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False