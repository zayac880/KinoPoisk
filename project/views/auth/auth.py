from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

api = Namespace('auth')


@api.route('/register')
class RegisterViews(Resource):
    def post(self):
        data = request.json
        """
        register email, password.
        """
        email = data.get("email")
        password = data.get("password")

        if None in [email, password]:
            return "", 400

        user_service.create(data)

        return "", 201


@api.route('/login')
class LoginView(Resource):
    def post(self):
        data = request.json
        """
        User has been authenticated, we return a response to the user in the form
    {
   "access_token": "qwesfsdfa",
   "refresh_token": "kjhgfgjakda",
    }
        """
        email = data.get('email')
        password = data.get('password')
        if not all([email, password]):
            return "", 400

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        data = request.json
        """
        Refresh token.
        """
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        tokens = auth_service.approve_refresh_token(access_token, refresh_token)

        return tokens, 200
