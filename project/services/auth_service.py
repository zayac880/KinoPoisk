import calendar
import datetime

import jwt

from constants import JWT_SECRET, JWT_ALGORITHM
from project.services.users_service import UsersService


class AuthService:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

        data = {
            "email": user.email,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, JWT_ALGORITHM)
        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data.get("email")

        user = self.user_service.get_user_by_email(email=email)

        if user is None:
            raise Exception(f"{email}Пользователь не найден")
        return self.generate_tokens(email, user.password, is_refresh=True)


