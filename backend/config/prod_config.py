from .base_config import BaseConfig


class ProdConfig(BaseConfig):
    """Production config class."""

    # Close the DEBUG
    DEBUG = False

    # MySQL connection
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://temp:temp@localhost:3306/temp'
    SQLALCHEMY_NATIVE_UNICODE = 'utf8'

    # Safe settings
    JWT_SECRET_KEY = 'How are you?I am fine, thank you!'
    CSRF_ENABLED = True
    JWT_HEADER_NAME = 'X-TOKEN'
    JWT_HEADER_TYPE = 'Knock'
    JWT_BLACKLIST_ENABLED = True
    # JWT_ACCESS_TOKEN_EXPIRES = False
