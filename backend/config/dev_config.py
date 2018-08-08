from .base_config import BaseConfig


class DevConfig(BaseConfig):
    """Development config class."""

    # Open the DEBUG
    DEBUG = True

    # MySQL connection
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:center135@localhost:3306/yijiublog'

    # Safe settings
    JWT_SECRET_KEY = 'How are you?I am fine, thank you!'
    CSRF_ENABLED = True
    JWT_HEADER_NAME = 'X-TOKEN'
    JWT_HEADER_TYPE = 'Knock'
    JWT_BLACKLIST_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False

    # Swagger settings
    SWAGGER = {
        "title": "YiJiuBlog backend API's Documents",
        "description": "This is an API's Documents about YiJiuBlog based on Swagger",
        "version": "0.0.2",
    }
