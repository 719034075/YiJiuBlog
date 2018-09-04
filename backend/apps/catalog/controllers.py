from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required

from apps.article.models import Article
from utils.json_serialize import list_json_serialize
from utils.response_bean import ResponseBean
from utils.protect_restful import requires_roles
from extensions import db
from .models import Catalog

catalog = Blueprint('catalog', __name__,
                    url_prefix='/catalog')

api = Api(catalog)


class Create(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, location='json', required=True)

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        args = self.parser.parse_args()
        name = args['name']

        if name == "默认":
            response = ResponseBean().get_fail_instance()
            response.message = '默认Catalog不可新建'
            return response.__dict__
        new_catalog = Catalog(name=name)
        db.session.add(new_catalog)
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '新建Catalog成功'
        return response.__dict__


class Delete(Resource):

    @jwt_required
    @requires_roles('superuser')
    def get(self, id):
        delete_catalog = Catalog.query.get(id)
        default_catalog = Catalog.query.filter_by(name="默认").first()
        if delete_catalog.name == "默认":
            response = ResponseBean().get_fail_instance()
            response.message = '默认Catalog不可删除'
            return response.__dict__
        articles = Article.query.filter_by(catalog=id)

        for article in articles:
            article.catalog = default_catalog.id
        default_catalog.amount = default_catalog.amount + delete_catalog.amount
        db.session.delete(delete_catalog)
        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '删除Catalog成功'
        return response.__dict__


class Update(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=str, location='json', required=True)
        self.parser.add_argument('name', type=str, location='json', required=True)

    @jwt_required
    @requires_roles('superuser')
    def post(self):
        args = self.parser.parse_args()
        id = args['id']
        name = args['name']

        edit_catalog = Catalog.query.filter_by(id=id).first()
        edit_catalog.name = name

        db.session.commit()

        response = ResponseBean().get_success_instance()
        response.message = '编辑Catalog成功'
        return response.__dict__


class Detail(Resource):
    @jwt_required
    @requires_roles('superuser')
    def get(self, id):
        find_catalog = Catalog.query.get(id)

        response = ResponseBean().get_success_instance()
        response.message = '查询Catalog成功'
        response.data['id'] = find_catalog.id
        response.data['name'] = find_catalog.name
        response.data['amount'] = find_catalog.amount

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

        catalogs = Catalog.query.order_by(Catalog.name).paginate(page, page_size)

        response = ResponseBean().get_success_instance()
        response.message = '查询Catalog成功'
        response.data['total'] = catalogs.pages
        response.data['results'] = list_json_serialize(catalogs.items)
        return response.__dict__

    @jwt_required
    @requires_roles('superuser')
    def get(self):
        catalogs = Catalog.query.order_by(Catalog.name).all()

        response = ResponseBean().get_success_instance()
        response.message = '查询Catalog成功'
        response.data['results'] = list_json_serialize(catalogs)
        return response.__dict__


api.add_resource(Create, '/create')
api.add_resource(Delete, '/delete/<string:id>')
api.add_resource(Update, '/update')
api.add_resource(Detail, '/detail/<string:id>')
api.add_resource(ListAll, '/list/all')
