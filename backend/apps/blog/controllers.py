from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, jwt_optional, get_raw_jwt
from utils.response_bean import ResponseBean
from utils.protect_restful import requires_roles
from extensions import jwt
from .models import Blog

blog = Blueprint('blog', __name__,
                 url_prefix='/blog')

api = Api(blog)


class Create(Resource):
    pass


class Delete(Resource):
    pass


class Edit(Resource):
    pass


class FindById(Resource):
    pass


class FindAll(Resource):
    pass


api.add_resource(Create, '/login')
api.add_resource(Delete, '/delete')
api.add_resource(Edit, '/edit')
api.add_resource(FindById, '/find-by-id')
api.add_resource(FindAll, '/find-all')

