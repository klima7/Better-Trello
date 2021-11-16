import os


class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1) \
        if 'DATABASE_URL' in os.environ else 'sqlite:///../app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'very-secret-key'
    CORS_EXPOSE_HEADERS = ['Authorization']
