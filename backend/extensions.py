from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flasgger import Swagger

# Create the Flask-SQLAlchemy's instance
db = SQLAlchemy()

# Create the Flask-Bcrypt's instance
bcrypt = Bcrypt()

# Create the Flask-CORS's instance
cors = CORS()

# Create the Flask-Restful's instance
restful_api = Api()

# Create the Flask-Httpauth's instance
auth = HTTPBasicAuth()

# Create the Flask-JWT-Extended's instance
jwt = JWTManager()

# Create the flasgger's instance
swagger = Swagger()
