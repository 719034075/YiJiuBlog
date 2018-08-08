from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, jwt_optional, get_raw_jwt
from utils.response_bean import ResponseBean
from utils.protect_restful import requires_roles
from extensions import jwt
from .models import User

user = Blueprint('user', __name__,
                 url_prefix='/user')
api = Api(user)

blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


# class SignUp(Resource):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('username', type=str, location='json')
#         self.parser.add_argument('password', type=str, location='json')
#
#     def post(self):
#         args = self.parser.parse_args()
#         username = args['username']
#         password = args['password']
#
#         if not username:
#             response = ResponseBean().get_fail_instance()
#             response.message = '用户名为空'
#             return response.__dict__
#
#         if not password:
#             response = ResponseBean().get_fail_instance()
#             response.message = '密码为空'
#             return response.__dict__
#
#         new_user = User(username=username, password=password)
#         add_user(new_user)
#
#         response = ResponseBean().get_success_instance()
#         response.message = '注册成功'
#         return response.__dict__


class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, location='json', required=True)
        self.parser.add_argument('password', type=str, location='json', required=True)

    def post(self):
        """
        登录
        用户登录接口
        ---
        tags:
          - user
        parameters:
          - in: body
            name: body
            schema:
               type: object
               required:
                 - username
                 - password
               properties:
                 username:
                   type: string
                   default: temp-admin
                 password:
                   type: string
                   default: temp-pwd
        responses:
          200:
            description: an access_token
            schema:
              properties:
                success:
                  type: boolean
                  description: return a successful response or not
                  default: True
                message:
                  type: string
                  description: return the response message
                  default: 登录成功
                data:
                  type: object
                  description: return the response data
                  default:
                    token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MjU1NzUyNDEsIm5iZiI6MTUyNTU3NTI0MSwianRpIjoiZjlhYjg2YTktZmU1Ny00ZDQyLWEzMmUtOWRhNGU5NjA4YWJmIiwiZXhwIjoxNTI1NTc2MTQxLCJpZGVudGl0eSI6InRlbXAtYWRtaW4iLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.9s9NbJsi21Kv5YbQaFuUXEqnFHsXd8FmAf2Q2wh_k6I

         """
        args = self.parser.parse_args()
        username = args['username']
        password = args['password']

        if not username:
            response = ResponseBean().get_fail_instance()
            response.message = '用户名为空'
            return response.__dict__

        if not password:
            response = ResponseBean().get_fail_instance()
            response.message = '密码为空'
            return response.__dict__

        login_user = User.query.filter_by(username=username).first()

        if login_user is None or not login_user.check_password(password=password):
            response = ResponseBean().get_fail_instance()
            response.message = '用户名或密码错误。'
            return response.__dict__

        access_token = create_access_token(identity=username)
        response = ResponseBean().get_success_instance()
        response.message = '登录成功'
        response.data['token'] = access_token
        return response.__dict__


class Info(Resource):
    @jwt_required
    def get(self):
        """
        用户信息
        登录之后通过token获取用户基本信息接口
        ---
        tags:
          - user
        parameters:
          - in: header
            name: X-TOKEN
            type: string
            required: true
            description: Knock <access_token>
        responses:
          200:
            description: 包括roles在内的用户基本信息
            schema:
              properties:
                success:
                  type: boolean
                  description: return a successful response or not
                  default: True
                message:
                  type: string
                  description: return the response message
                  default: 获取用户信息成功
                data:
                  type: object
                  description: return the response data
                  default:
                    roles: superuser
                    name: temp-admin
                    avatar: nope
         """
        jwt_user = get_jwt_identity()
        if jwt_user:
            current_user = User.query.filter_by(username=jwt_user).first()
            response = ResponseBean().get_success_instance()
            response.message = '获取用户信息成功'
            response.data['roles'] = [current_user.roles]
            response.data['name'] = current_user.username
            response.data['avatar'] = current_user.avatar
            return response.__dict__
        else:
            response = ResponseBean().get_fail_instance()
            response.message = '非法用戶'
            return response.__dict__


class Logout(Resource):
    @jwt_required
    def post(self):
        """
        登出
        用户登出接口
        ---
        tags:
          - user
        parameters:
          - in: header
            name: X-TOKEN
            type: string
            required: true
            description: Knock <access_token>
        responses:
          200:
            description: 无
            schema:
              properties:
                success:
                  type: boolean
                  description: return a successful response or not
                  default: True
                message:
                  type: string
                  description: return the response message
                  default: 登出成功
         """
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        response = ResponseBean().get_success_instance()
        response.message = '登出成功'
        return response.__dict__


# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
class Protect(Resource):
    @jwt_required
    @requires_roles('superuser')
    def get(self):
        current_user = get_jwt_identity()
        response = ResponseBean().get_success_instance()
        response.message = '登录用户'
        response.data['logged_in_as'] = current_user
        return response.__dict__


class PartiallyProtected(Resource):
    @jwt_optional
    def get(self):
        # If no JWT is sent in with the request, get_jwt_identity()
        # will return None
        current_user = get_jwt_identity()
        if current_user:
            response = ResponseBean().get_success_instance()
            response.message = '登录用户'
            response.data['logged_in_as'] = current_user
            return response.__dict__
        else:
            response = ResponseBean().get_success_instance()
            response.message = '匿名用户'
            response.data['logged_in_as'] = 'anonymous  user'
            return response.__dict__


api.add_resource(Login, '/login')
api.add_resource(Info, '/info')
api.add_resource(Logout, '/logout')
api.add_resource(Protect, '/protect')
api.add_resource(PartiallyProtected, '/partially-protected')
