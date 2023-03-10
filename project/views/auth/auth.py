from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service

api = Namespace('auth')


@api.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')
        if not all([username, password]):
            return "", 400

        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201