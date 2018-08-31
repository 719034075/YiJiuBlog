import time
from datetime import datetime
from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required

from utils.json_serialize import list_json_serialize
from utils.response_bean import ResponseBean
from utils.protect_restful import requires_roles
from extensions import db
from .models import Article
from apps.catalog.models import Catalog

article = Blueprint('article', __name__,
                    url_prefix='/article')

api = Api(article)


class Create(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title', type=str, location='json', required=True)
        self.parser.add_argument('author', type=str, location='json', required=True)
        self.parser.add_argument('catalog', type=str, location='json', required=True)
        self.parser.add_argument('abstract', type=str, location='json')
        self.parser.add_argument('content', type=str, location='json')
        self.parser.add_argument('status', type=str, location='json', required=True)

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        args = self.parser.parse_args()
        title = args['title']
        author = args['author']
        catalog = args['catalog']
        abstract = args['abstract']
        content = args['content']
        status = args['status']

        now_time = datetime.now()
        new_article = Article(title=title, author=author, catalog=catalog, abstract=abstract, content=content,
                              create_time=now_time,
                              update_time=now_time, status=status)
        db.session.add(new_article)
        find_catalog = Catalog.query.get(catalog)
        find_catalog.amount = find_catalog.amount + 1
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '新建Article成功'
        return response.__dict__


class Delete(Resource):

    @jwt_required
    @requires_roles('superuser')
    def get(self, id):
        delete_article = Article.query.get(id)
        db.session.delete(delete_article)

        find_catalog = Catalog.query.get(delete_article.catalog)
        find_catalog.amount = find_catalog.amount - 1
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '删除Article成功'
        return response.__dict__


class Update(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=str, location='json', required=True)
        self.parser.add_argument('title', type=str, location='json', required=True)
        self.parser.add_argument('author', type=str, location='json')
        self.parser.add_argument('catalog', type=str, location='json', required=True)
        self.parser.add_argument('abstract', type=str, location='json')
        self.parser.add_argument('content', type=str, location='json')
        self.parser.add_argument('status', type=str, location='json', required=True)

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        args = self.parser.parse_args()
        id = args['id']
        title = args['title']
        author = args['author']
        catalog = args['catalog']
        abstract = args['abstract']
        content = args['content']
        status = args['status']

        edit_article = Article.query.filter_by(id=id).first()
        edit_article.title = title
        edit_article.author = author
        edit_article.catalog = catalog
        edit_article.abstract = abstract
        edit_article.content = content
        edit_article.update_time = datetime.now()
        edit_article.status = status
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '编辑Article成功'
        return response.__dict__


class Detail(Resource):
    @jwt_required
    @requires_roles('superuser')
    def get(self, id):
        find_article = Article.query.get(id)
        find_catalog = Catalog.query.get(find_article.catalog)

        response = ResponseBean().get_success_instance()
        response.message = '查询Article成功'
        response.data['id'] = find_article.id
        response.data['title'] = find_article.title
        response.data['author'] = find_article.author
        response.data['catalog'] = find_catalog.name
        response.data['abstract'] = find_article.abstract
        response.data['content'] = find_article.content
        response.data['create_time'] = time.mktime(find_article.create_time.timetuple()) * 1000
        response.data['update_time'] = time.mktime(find_article.update_time.timetuple()) * 1000
        response.data['status'] = find_article.status

        return response.__dict__


class ListAll(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('page', type=int, location='json', required=True)
        self.parser.add_argument('page_size', type=int, location='json', required=True)

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        args = self.parser.parse_args()
        page = args['page']
        page_size = args['page_size']

        articles = Article.query.order_by(Article.create_time).paginate(page, page_size)

        response = ResponseBean().get_success_instance()
        response.message = '查找Articles成功'
        response.data['total'] = articles.pages
        response.data['results'] = list_json_serialize(articles.items)
        return response.__dict__


class ListPublished(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('page', type=int, location='json', required=True)
        self.parser.add_argument('page_size', type=int, location='json', required=True)

    def post(self):
        args = self.parser.parse_args()
        page = args['page']
        page_size = args['page_size']

        articles = Article.query.order_by(Article.create_time).filter_by(status='published').paginate(page, page_size)

        response = ResponseBean().get_success_instance()
        response.message = '查找Articles成功'
        response.data['total'] = articles.pages
        response.data['results'] = list_json_serialize(articles.items)
        return response.__dict__


api.add_resource(Create, '/create')
api.add_resource(Delete, '/delete/<string:id>')
api.add_resource(Update, '/update')
api.add_resource(Detail, '/detail/<string:id>')
api.add_resource(ListAll, '/list/all')
api.add_resource(ListPublished, '/list/published')
