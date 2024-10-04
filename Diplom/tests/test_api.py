import allure
import pytest
from Pages.page_api import ApiKinopoisk


api_kinopoisk = ApiKinopoisk()

@allure.id("Diplom-API-1")
@allure.severity("critical")
@allure.story("Поиск фильма по ID")
@allure.epic("API-Kinopoisk")
@allure.feature("GET_info")
@allure.title("Поиск фильма по ID с получением информации от сервера")
@allure.description("Запрос на поиск фильма с указанием film_id и названием фильма 1+1")
def test_poisk_by_id():
    with allure.step("Создаем переменную с айди фильма"):
        film_id = 535341
    with allure.step("Получить фильм через АПИ"):
        response = api_kinopoisk.get_film_by_id(film_id)
    with allure.step("Сравнить статус код"):
        assert response.status_code == 200
    with allure.step("Получить ответ в формате json"):
        response_data = response.json()
    with allure.step("Сравнить ответ от сервера с заданым названием фильма"):
        assert response_data["name"] == "1+1"
    with allure.step("Сравнить headers c ответом от сервера"):
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

@allure.id("Diplom-API-2")
@allure.severity("critical")
@allure.story("Получение рандомного тайтла с рейтингом")
@allure.epic("API-Kinopoisk")
@allure.feature("GET_info")
@allure.title("Поиск фильма по рандомному тайтлу")
@allure.description("Запрос на поиск рандомного тайтла с указанием рейтинга фильма и возраста")
def test_random_title_with_rating():
    with allure.step("Получаем рандомный фильм с указанными параметрами поиска"):
        response = api_kinopoisk.get_random_title_with_rating(min_rating=8, age_rating=18)
    with allure.step("Сравниваем статус-код"):
        assert response.status_code == 200
    with allure.step("Проверить из ответа в формате json возраст"):
        response_data = response.json()
        assert response_data["ageRating"] == 18

@allure.id("Diplom-API-3")
@allure.severity("critical")
@allure.story("Негативный отзыв с автором")
@allure.epic("API-Kinopoisk")
@allure.feature("Rewiew")
@allure.title("Негативный отзыв с отображением автора")
@allure.description("Запрос на негативный отзыв с автором")
def test_negative_rewiew_with_autor():
    with allure.step("Получаем неагативный отзыв с автором из АПИ"):
        response = api_kinopoisk.get_negative_reviews_with_author(page=1, limit=3)
    with allure.step("Проверить из ответа статус код и вид отзыва"):
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["docs"][0]["type"] == "Негативный"

@allure.id("Diplom-API-4")
@allure.severity("critical")
@allure.story("Поиск по номинации")
@allure.epic("API-Kinopoisk")
@allure.feature("GET_info")
@allure.title("Поиск фильмов по номинации")
@allure.description("Запрос на поиск фильма с указанием номинации 'Oscar'")
def test_find_by_nomination_title():
    with allure.step("Поиск по номинациям Оскар тайтлов через АПИ"):
        response = api_kinopoisk.find_by_nomination_title(nomination="Oscar", page=1, limit=10)
    with allure.step("Проверить статус код ответа"):
        assert response.status_code == 200

@allure.id("Diplom-API-5")
@allure.severity("critical")
@allure.story("Поиск по имени актера")
@allure.epic("API-Kinopoisk")
@allure.feature("GET_info")
@allure.title("Получение информации о актере")
@allure.description("Запрос на поиск информации о актере с указанием актера")
def test_find_by_name_actor():
    with allure.step("Поиск информации по имени актера через АПИ"):
        response = api_kinopoisk.find_by_name_actor(name="Джонни Дэпп", page=1, limit=1)
    with allure.step("Проверить из ответа сервера статус кода и возраста актера"):
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["docs"][0]["age"] == 61