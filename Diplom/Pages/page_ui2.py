import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
import allure
from tests.constants import Kinopoisk_base_url

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для работы с элементами на странице, такие как клик и ввод текста.
    """

    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        :param driver: объект веб-драйвера Selenium.
        """
        self.driver = driver

    def find_and_click(self, by_locator,):
        """
        Поиск элемента и выполнение клика.
        :param by_locator: локатор элемента (тип и значение).
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def find_and_type(self, by_locator, text):
        """
        Поиск элемента и ввод текста.
        :param by_locator: локатор элемента (тип и значение).
        :param text: текст, который необходимо ввести.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

class MainPage(BasePage):
    @allure.step("Открыть базовую страницу кинопоиска")
    def open(self):
        """
        Открывает страницу кинопоиска.
        """
        self.driver.get(Kinopoisk_base_url)

    @allure.step("Поиск в шапке страницы в поле поиск")
    def search_by_head(self,name_film):
        self.find_and_type((By.CSS_SELECTOR,'input[name="kp_query"'), name_film)
        self.find_and_click((By.CSS_SELECTOR, 'button[type="submit"'))

    @allure.step("Поиск в шапке страницы используя расширенный поиск")
    def open_super_search(self):
        self.find_and_click((By.CSS_SELECTOR,'[aria-label="Расширенный поиск"]'))

    @allure.step("Скролл страницы вниз-1")
    def scroll_down(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Скролл страницы вниз-2")
    def scroll_2(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break 
            last_height = new_height

    @allure.step("Поиск селектора поддержки")
    def find_support(self):
        self.find_and_click((By.XPATH,"//button[@class='styles_contentButton__Yfvdh']"))

    def ok_cookie(self):
        self.find_and_click((By.CSS_SELECTOR,'data-test-tag="confirm-dialog-ok"'))


class highSearch(BasePage):

    @allure.step("Поиск по топ фильмов")
    def search_by_top(self):
        self.find_and_click((By.CSS_SELECTOR,'a[class="all"]'))

    @allure.step("Скролл страницы вниз")
    def scroll_1(self):
        self.driver.execute_script("window.scrollBy(0,400)")

    @allure.step("Вызов выпадающего списка жанров")
    def spisok_ganrov(self):
        self.find_and_click((By.XPATH, '//*[@id="genreListTitle"]'))

    @allure.step("Ожидание элемента аниме")
    def wait_list(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-name="аниме"]')))

    @allure.step("Нажатие на кнопку аниме")
    def click_anime(self):
        self.find_and_click((By.CSS_SELECTOR,'input[data-name="аниме"]'))

    @allure.step("Ожидание списка")
    def wait_spisok(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="genreListTitle"]')))

    @allure.step("Ожидание кнопки поиск")
    def wait_poisk(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="nice_button submit"]')))

    @allure.step("Нажать кнопку поиск")
    def click_poisk(self):
        self.find_and_click((By.XPATH, '//*[@class="nice_button submit"]'))

    @allure.step("Ожиадние результатов поиска")
    def wait_table(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element((By.ID,"itemList")))

    @allure.step("Скролл до кнопки поиск")
    def scroll_to_poisk(self):
        self.driver.execute_script("window.scrollBy(0,800)")

    @allure.step("Скролл до резултатов поиска")
    def scrol_to_table(self):
        self.driver.execute_script("window.scrollBy(0,800)")

    @allure.step("Ожидание списка звезд рейтинга")
    def wait_star(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class="s10"]')))

    @allure.step("Нажать на звезду")
    def click_star(self):
        self.find_and_click((By.CSS_SELECTOR, 'a[class="s10"]'))

