import pytest

from project.dao.main import MoviesDAO
from project.models import Movie


class TestMoviesDAO:

    @pytest.fixture
    def movies_dao(self, db):
        return MoviesDAO(db.session)

    @pytest.fixture
    def movie_1(self, db):
        m = Movie(title='Йеллоустоун',
        description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
        year=2018,
        rating=8.6)
        db.session.add(m)
        db.session.commit()
        return m

    @pytest.fixture
    def movie_2(self, db):
        m = Movie(title='',
        description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        trailer="https://www.youtube.com/watch?v=UKei_d0cbP4",
        year=2018,
        rating=8.6)
        db.session.add(m)
        db.session.commit()
        return m

    def test_get_movie_by_id(self, movie_1, movies_dao):
        assert movies_dao.get_by_id(movie_1.id) == movie_1

    def test_get_movie_by_id_not_found(self, movies_dao):
        assert not movies_dao.get_by_id(1)

    def test_get_all_movies(self, movies_dao, movie_1, movie_2):
        assert movies_dao.get_all() == [movie_1, movie_2]

    def test_get_movies_by_page(self, app, movies_dao, movie_1, movie_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert movies_dao.get_all(page=1) == [movie_1]
        assert movies_dao.get_all(page=2) == [movie_2]
        assert movies_dao.get_all(page=3) == []