from Pages.page_ui2 import MainPage
from Pages.page_ui2 import highSearch
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure


@pytest.fixture
def browser():
    """
    Фикстура для создания и закрытия экземпляра веб-драйвера.
    :return: объект веб-драйвера Selenium.
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

@allure.id("Diplom-UI-1")
@allure.severity("Blocker")
@allure.story("Поиск фильма")
@allure.epic("UI Kinopoisk")
@allure.feature("Тест-1")
@allure.title("Поиск фильма в поле поиска")
@allure.description("Поиск фильма 'Король и шут' в шапке страницы в поле поиск")
def test_search_film(browser):
    with allure.step("инициализация базовой страницы и драйвера"):
        Main_paige = MainPage(browser)
    with allure.step("Открыть главную страницу сайта"):
        Main_paige.open()
    with allure.step("Поиск в шапке страницы фильма"):
        Main_paige.search_by_head("Король и Шут")

@allure.id("Diplom-UI-2")
@allure.severity("Blocker")
@allure.story("Поиск фильма")
@allure.epic("UI Kinopoisk")
@allure.feature("Тест-2")
@allure.title("Пeреход на вкладку с расширенным поиском")
@allure.description("Переход в расширенный поиск")
def test_super_search_film(browser):
    with allure.step("инициализация базовой страницы и драйвера"):
        Main_paige = MainPage(browser)
    with allure.step("Открыть главную страницу сайта"):
        Main_paige.open()
    with allure.step("Открыть меню расширеного поиска"):
        Main_paige.open_super_search()

@allure.id("Diplom-UI-3")
@allure.severity("Blocker")
@allure.story("Поиск фильма")
@allure.epic("UI Kinopoisk")
@allure.feature("Тест-3")
@allure.title("Переход на страницу с фильмами топ 250")
@allure.description("Переход в расширенный поиск с параметрами топ-250 фильмов")
def test_search_by_top(browser):
    with allure.step("инициализация базовой страницы и драйвера"):
        Main_paige = MainPage(browser)
    with allure.step("инициализация страницы с расширенным поиском"):
        High_search = highSearch(browser)
    while allure.step("Открыть главную страницу сайта"):
        Main_paige.open()
    with allure.step("Открыть меню расширеного поиска"):
        Main_paige.open_super_search()
    with allure.step("открыть поиск по топ фильмам"):
        High_search.search_by_top()

@allure.id("Diplom-UI-4")
@allure.severity("Critical")
@allure.story("Поиск фильма")
@allure.epic("UI Kinopoisk")
@allure.feature("Тест-4")
@allure.title("Переход на страницу с фильмами топ аниме")
@allure.description("Переход на страницу с результами поиска по ТОП Аниме фильмам")
def test_search_anime_film_top(browser):
    with allure.step("инициализация базовой страницы и драйвера"):
        Main_paige = MainPage(browser)
    with allure.step("инициализация страницы с расширенным поиском"):
        High_search = highSearch(browser)
    with allure.step("Открыть главную страницу сайта"):
        Main_paige.open()
    with allure.step("Открыть меню расширеного поиска"):
        Main_paige.open_super_search()
    with allure.step("открыть поиск по топ фильмам"):
        High_search.search_by_top()
    with allure.step("Проскролить страницу до нужного элемента"):
        High_search.scroll_1()
    with allure.step("Нажать на список жанров"):
        High_search.spisok_ganrov()
    with allure.step("Ожидание выпадающего списка"):
        High_search.wait_list()
    with allure.step("Нажать на кнопку 'аниме'"):
        High_search.click_anime()
    with allure.step("Ожидание выпадающего списка"):
        High_search.wait_spisok()
    with allure.step("Нажать на список жанров"):
        High_search.spisok_ganrov()
    with allure.step("Скролл до кнопки поиска"):
        High_search.scroll_to_poisk()
    with allure.step("Ожидаем кнопку поиск"):
        High_search.wait_poisk()
    with allure.step("Нажать на кнопку поиск"):
        High_search.click_poisk()
    with allure.step("Ожидание списка"):
        High_search.wait_table()
    with allure.step("Скролл до таблицы"):
        High_search.scrol_to_table()
    with allure.step("Ожидаем появление звезд"):
        High_search.wait_star()
    with allure.step("Нажать на звезду"):
        High_search.click_star()

@allure.id("Diplom-UI-5")
@allure.severity("Blocker")
@allure.story("Support")
@allure.epic("UI Kinopoisk")
@allure.feature("Тест-5")
@allure.title("Обращение в поддержку")
@allure.description("Переход на форму обращения в тех.поддержку сайта")
def test_write_to_support(browser):
    with allure.step("инициализация базовой страницы и драйвера"):
        Main_paige = MainPage(browser)
    with allure.step("инициализация неявного ожидания"):
        Main_paige.driver.implicitly_wait(2)
    with allure.step("Открыть главную страницу сайта"):
        Main_paige.open()
    with allure.step("Скролл вниз сайта"):
        Main_paige.scroll_2()
    with allure.step("нажать на кнопку 'поддержка'"):
        Main_paige.find_support()