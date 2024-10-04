import allure
import requests
from tests.constants import API_base_url
from tests.conftest import token

class ApiKinopoisk:
    """
    Базовый класс для АПИ кинопоиск
    """

    def __init__(self):
        """Инициализация и запуск АПИ, содержит токен и базовый url """
        self.base_url = API_base_url
        self.headers = token

    def get_film_by_id(self, film_id):
        """Поиск фильма по id
        :param film_id: id фильма(цифровое значение)"""
        response = requests.get(f"{self.base_url}movie/{film_id}", headers=self.headers)
        return response

    def get_random_title_with_rating(self, min_rating=8, age_rating=18):
        """Поиск рандомного фильма с указанием рейтинга
        :param min_rating,age_rating:рейтинг кп, рейтинг возраста(цифровое значение)"""
        params = {
            "rating.kp": min_rating,
            "ageRating": age_rating
        }
        response = requests.get(f"{self.base_url}movie/random", headers=self.headers, params=params)
        return response

    def get_negative_reviews_with_author(self, page=1, limit=3):
        """Поиск негативного отзыва с сортировкой по автору
        :param page: страница(цифровое значение),limit: лимит отображения результатов(цифровое значение)"""
        params = {
            "page": page,
            "limit": limit,
            "sortField": "author",
            "sortType": 1,
            "type": "Негативный"
        }
        response = requests.get(f"{self.base_url}review", headers=self.headers, params=params)
        return response

    def find_by_nomination_title(self, nomination="Oscar", page=1, limit=10):
        """Поиск фильма по номинациям
        :param nomination: номинация фильма(ключ-значение)
        :param page/limit: страница/количество отображаемых результатов"""
        params = {
            "page": page,
            "limit": limit,
            "nomination.title": nomination
        }
        response = requests.get(f"{self.base_url}person/awards", headers=self.headers, params=params)
        return response

    def find_by_name_actor(self, name="Джонни Дэпп", page=1, limit=1):
        """Поиск результатов по имени акетра
        :param name: имя акетра(ключ-значение)
        :param page/limit: страница/количество отображаемых результатов"""
        params = {
            "page": page,
            "limit": limit,
            "query": name
        }
        response = requests.get(f"{self.base_url}person/search", headers=self.headers, params=params)
        return response