from flask import request
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

api = Namespace('auth')


@api.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')
        if not all([email, password]):
            return "", 400

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        data = request.json

        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        validated = auth_service.validate_tokens(access_token, refresh_token)

        if not validated:
            return "Invalid tokens", 400

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201


@api.route('/register')
class RegisterViews(Resource):
    def post(self):
        data = request.json

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
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return {"message": "Email and password are required"}, 400

        user = user_service.get_user_by_email(email)
        if not user:
            return {"message": "Invalid credentials"}, 401

        if not user_service.compare_passwords(user, password):
            return {"message": "Invalid credentials"}, 401

        access_token, refresh_token = auth_service.generate_tokens(user)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200