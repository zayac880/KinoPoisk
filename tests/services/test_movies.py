from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.models import Movie
from project.services.movies_service import MoviesService


class TestMoviesService:

    @pytest.fixture()
    @patch('project.dao.main.MoviesDAO')
    def movies_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Movie(id='id', title='Йеллоустоун', description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»', trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', year=2018,rating=8.6)
        dao.get_all.return_value = [
            Movie(id='id', title='Йеллоустоун', description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»', trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', year=2018,rating=8.6),
            Movie(id='id', title='Йеллоустоун', description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»', trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', year=2018,rating=8.6),
        ]
        return dao

    @pytest.fixture()
    def movies_service(self, movies_dao_mock):
        return MoviesService(dao=movies_dao_mock)

    @pytest.fixture
    def movie(self, db):
        obj = Movie(title="movie")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_movie(self, movies_service, movie):
        assert movies_service.get_item(movie.id)

    def test_movie_not_found(self, movies_dao_mock, movies_service):
        movies_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            movies_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_movies(self, movies_dao_mock, movies_service, page):
        movies = movies_service.get_all(page=page)
        assert len(movies) == 2
        assert movies == movies_dao_mock.get_all.return_value
        movies_dao_mock.get_all.assert_called_with(page=page)