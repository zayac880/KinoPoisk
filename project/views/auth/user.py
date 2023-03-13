from flask import request
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
        Get all users.
        """
        return user_service.get_all()


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        Get user by id.
        """
        return user_service.get_one(user_id)

    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def patch(self, user_id: int):
        """
        Update user by id.
        """
        user_data = api.payload
        user_data['id'] = user_id
        user_service.update_users(user_data)
        return None, 200


@api.route('/password')
class UserView(Resource):
    def put(self):
        data = request.json

        email = data.get("email")
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        user = user_service.get_user_by_email(email)

        if user_service.compare_passwords(user.password, old_password):
            # user.password = user_service.make_user_password_hash(new_password)
            user_service.update_password({
                "id": user.id,
                "password": new_password
            })
            return "Password changed successfully", 201
        else:
            return "Password did not changed", 400
