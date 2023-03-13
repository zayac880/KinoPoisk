from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.setup.api.parsers import page_parser

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return user_service.get_all()


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        Get genre by id.
        """
        return user_service.get_one(user_id)

    @api.expect(user)
    @api.response(404, 'Not Found')
    @api.response(200, 'OK')
    def patch(self, user_id: int):
        """
        Update user by id.
        """
        user_data = api.payload
        user_data['id'] = user_id
        user_service.update(user_data)
        return None, 200


@api.route('/password')
class UserView(Resource):
    def put(self):
        pass
