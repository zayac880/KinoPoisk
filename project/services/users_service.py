import base64
import hashlib
import hmac

from project.dao.user_dao import UsersDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UsersService:
    def __init__(self, dao: UsersDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_user_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, user_data):
        user_data['password'] = self.make_user_password_hash(user_data.get('password'))
        return self.dao.create(user_data)


    def delete(self, uid):
        self.dao.delete(uid)

    def make_user_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS,
        ))

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            password_hash,
            self.make_user_password_hash(other_password),
        )

    def update_password(self, data):
        data['password'] = self.make_user_password_hash(data.get('password'))
        self.dao.update_password(data)
        return self.dao

    def update_users(self, user_data):
        self.dao.update_user(user_data)
        return self.dao
