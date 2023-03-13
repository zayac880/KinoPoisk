from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import User
from project.setup.api.models import user
from project.setup.api.parsers import page_parser

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all users.
        """
        return user_service.get_all()


    def patch(self):
        pass


@api.route('/password')
class UserView(Resource):
    def put(self):
        pass
