from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import User

api = Namespace('user')


@api.route('/')
class UserView(Resource):
    def get(self):
        pass

    def patch(self):
        pass


@api.route('/password')
class UserView(Resource):
    def put(self):
        pass
