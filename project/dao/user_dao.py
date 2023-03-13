from typing import Optional

from project.models import User


class UsersDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.email == username).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter_by(email=email).first()

    def create(self, user_data):
        ent = User(**user_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update_user(self, user_data):
        user = self.get_one(user_data.get("id"))
        user.name = user_data.get("name")
        user.surname = user_data.get("surname")
        user.favorite_genre = user_data.get("favorite_genre")

        self.session.add(user)
        self.session.commit()

    def update_password(self, data):
        user = self.get_one(data.get("id"))
        user.password = data.get("password")

        self.session.add(user)
        self.session.commit()
