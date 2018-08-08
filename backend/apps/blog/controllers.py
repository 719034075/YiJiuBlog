from datetime import datetime
from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, jwt_optional, get_raw_jwt
from utils.response_bean import ResponseBean
from utils.protect_restful import requires_roles
from extensions import jwt, db
from .models import Blog

blog = Blueprint('blog', __name__,
                 url_prefix='/blog')

api = Api(blog)


class Create(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('author', type=str, location='json', required=True)
        self.parser.add_argument('title', type=str, location='json', required=True)
        self.parser.add_argument('context', type=str, location='json')

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        """
                新建
                新建Blog接口
                ---
                tags:
                  - blog
                parameters:
                  - in: body
                    name: body
                    schema:
                       type: object
                       required:
                         - author
                         - title
                       properties:
                         author:
                           type: string
                           default: temp-admin
                         title:
                           type: string
                           default: temp-title
                         context:
                           type: string
                           default: temp-context
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
                          default: 新建Blog成功

                 """
        args = self.parser.parse_args()
        author = args['author']
        title = args['title']
        context = args['context']

        if not author:
            response = ResponseBean().get_fail_instance()
            response.message = '作者为空'
            return response.__dict__

        if not title:
            response = ResponseBean().get_fail_instance()
            response.message = '标题为空'
            return response.__dict__

        now_time = datetime.now()
        new_blog = Blog(title=title, author=author, context=context, create_time=now_time, update_time=now_time)
        db.session.add(new_blog)
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '新建Blog成功'
        return response.__dict__


class DeleteById(Resource):

    @jwt_required
    @requires_roles('superuser')
    def get(self, id):
        """
                 删除
                 根据Id删除Blog接口
                 ---
                 tags:
                   - blog
                 parameters:
                   - in: path
                     name: id
                     type: string
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
                           default: 删除Blog成功

                  """
        delete_blog = Blog.query.get(id)
        if delete_blog is None:
            response = ResponseBean().get_fail_instance()
            response.message = '指定Blog不存在。'
            return response.__dict__

        db.session.delete(delete_blog)
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '删除Blog成功'
        return response.__dict__


class Edit(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=str, location='json', required=True)
        self.parser.add_argument('author', type=str, location='json', required=True)
        self.parser.add_argument('title', type=str, location='json', required=True)
        self.parser.add_argument('context', type=str, location='json')

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        """
                编辑
                编辑Blog接口
                ---
                tags:
                  - blog
                parameters:
                  - in: body
                    name: body
                    schema:
                       type: object
                       required:
                         - author
                         - title
                       properties:
                         id:
                           type: string
                         author:
                           type: string
                           default: temp-admin
                         title:
                           type: string
                           default: temp-title
                         context:
                           type: string
                           default: temp-context
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
                          default: 编辑Blog成功

                 """
        args = self.parser.parse_args()
        id = args['id']
        author = args['author']
        title = args['title']
        context = args['context']

        if not id:
            response = ResponseBean().get_fail_instance()
            response.message = 'Id为空'
            return response.__dict__

        if not author:
            response = ResponseBean().get_fail_instance()
            response.message = '作者为空'
            return response.__dict__

        if not title:
            response = ResponseBean().get_fail_instance()
            response.message = '标题为空'
            return response.__dict__

        edit_blog = Blog.query.filter_by(id=id).first()
        edit_blog.author = author
        edit_blog.title = title
        edit_blog.context = context
        edit_blog.update_time = datetime.now()
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '编辑Blog成功'
        return response.__dict__


class FindById(Resource):
    @jwt_required
    @requires_roles('superuser')
    def get(self, id):
        """
                 查询
                 根据Id查询Blog接口
                 ---
                 tags:
                   - blog
                 parameters:
                   - in: path
                     name: id
                     type: string
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
                           default: 查询Blog成功
                         data:
                            type: object
                            description: return the response data
                            default:
                                id: temp-id
                                title: temp-title
                                author: temp-author
                                context: temp-context
                                create_time: temp-time
                                update_time: temp-time
                  """
        find_blog = Blog.query.get(id)
        if find_blog is None:
            response = ResponseBean().get_fail_instance()
            response.message = '指定Blog不存在。'
            return response.__dict__

        response = ResponseBean().get_success_instance()
        response.message = '查询Blog成功'
        response.data['id'] = find_blog.id
        response.data['title'] = find_blog.title
        response.data['author'] = find_blog.author
        response.data['context'] = find_blog.context
        response.data['create_time'] = find_blog.create_time
        response.data['update_time'] = find_blog.update_time
        return response.__dict__


class FindByConditions(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('page', type=int, location='json', required=True)
        self.parser.add_argument('page_size', type=int, location='json', required=True)

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        """
                查询
                按条件查询Blog接口
                ---
                tags:
                  - blog
                parameters:
                  - in: body
                    name: body
                    schema:
                       type: object
                       required:
                         - author
                         - title
                       properties:
                         author:
                           type: string
                           default: temp-admin
                         title:
                           type: string
                           default: temp-title
                         page:
                           type: int
                           default: 1
                         pageSize:
                           type: int
                           default: 10

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
                          default: 查询Blog成功
                         data:
                            type: object
                            description: return the response data
                            default:
                                total: 100
                                results: []

                 """
        args = self.parser.parse_args()
        page = args['page']
        page_size = args['page_size']

        if not page:
            response = ResponseBean().get_fail_instance()
            response.message = 'page为空'
            return response.__dict__

        if not page_size:
            response = ResponseBean().get_fail_instance()
            response.message = 'pageSize为空'
            return response.__dict__

        blogs = Blog.query.order_by(Blog.create_time).paginate(page, page_size)

        response = ResponseBean().get_success_instance()
        response.message = '查找Blog成功'
        response.data['total'] = blogs.pages
        response.data['results'] = blogs.items
        return response.__dict__


api.add_resource(Create, '/create')
api.add_resource(DeleteById, '/delete-by-id/<string:id>')
api.add_resource(Edit, '/edit')
api.add_resource(FindById, '/find-by-id/<string:id>')
api.add_resource(FindByConditions, '/find-by-conditions')
