from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    @api.expect(404, 'Not Found')
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        """
        Получить всех пользователей.
        """
        return user_service.get_all()

    @api.expect(user)
    @api.response(201, 'Created')
    def post(self):
        """
        Создать нового пользователя.
        """
        new_user = user_service.create(api.payload)
        return new_user, 201


@api.route('/<int:user_id>/')
class UserView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(user, code=200, description='OK')
    def get(self, user_id: int):
        """
        Получить пользователя по идентификатору.
        """
        return user_service.get_one(user_id)

    @api.expect(user)
    @api.response(204, 'No Content')
    def put(self, user_id: int):
        """
        Обновить пользователя по идентификатору.
        """
        user_service.update(user_id, api.payload)
        return None, 204

    @api.response(204, 'No Content')
    def delete(self, user_id: int):
        """
        Удалить пользователя по идентификатору.
        """
        user_service.delete(user_id)
        return None, 204




