from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Директор', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тейлор Шеридан'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=15),
    'name': fields.String(required=True, max_length=100, example='Сияние'),
    'description': fields.String(required=True, max_length=255, example='Джек Торренс с женой и сыном приезжает в элегантный отдалённый отель, чтобы работать смотрителем во время мертвого сезона. Торренс здесь раньше никогда не бывал. Или это не совсем так? Ответ лежит во мраке, сотканном из преступного кошмара.'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtube.com/watch?v=NMSUEhDWXH0'),
    'year': fields.Integer(required=True, example=1980),
    'rating': fields.Float(required=True, example=8.4)
})

user: Model = api.model('пользователь', {
    'id': fields.Integer(required=True),
    'email ': fields.String(required=True),
    'password ': fields.String(required=True),
    'name': fields.String(required=True),
    'surname ': fields.String(required=True),
    'favorite_genre ': fields.String(required=True)
})
