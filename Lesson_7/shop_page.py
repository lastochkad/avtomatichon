import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def find_and_click(self, by_locator):
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


class LoginPage(BasePage):
    """
    Класс для страницы логина.
    Содержит методы для открытия страницы и авторизации пользователя.
    """

    def open(self):
        """
        Открывает страницу логина.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username="standard_user", password="secret_sauce"):
        """
        Выполняет авторизацию пользователя.
        :param username: имя пользователя (по умолчанию 'standard_user').
        :param password: пароль (по умолчанию 'secret_sauce').
        """
        self.find_and_type((By.ID, "user-name"), username)
        self.find_and_type((By.ID, "password"), password)
        self.find_and_click((By.ID, "login-button"))


class ProductsPage(BasePage):
    """
    Класс для страницы с товарами.
    Содержит методы для добавления товаров в корзину и перехода в корзину.
    """

    def add_products_to_cart(self, *product_ids):
        """
        Добавляет указанные товары в корзину.
        :param product_ids: идентификаторы товаров для добавления в корзину.
        """
        for product_id in product_ids:
            self.find_and_click((By.ID, f"add-to-cart-{product_id}"))

    def go_to_cart(self):
        """
        Переходит на страницу корзины.
        """
        self.find_and_click((By.CLASS_NAME, "shopping_cart_link"))


class CheckoutPage(BasePage):
    """
    Класс для страницы оформления заказа.
    Содержит метод для начала оформления заказа.
    """

    def proceed_to_checkout(self):
        """
        Начинает процесс оформления заказа.
        """
        self.find_and_click((By.ID, "checkout"))


class PersonalInfoPage(BasePage):
    """
    Класс для страницы ввода персональных данных.
    Содержит метод для заполнения формы с личной информацией.
    """

    def fill_personal_info(self, first_name, last_name, postal_code):
        """
        Заполняет форму с личной информацией.
        :param first_name: имя.
        :param last_name: фамилия.
        :param postal_code: почтовый индекс.
        """
        self.find_and_type((By.ID, "first-name"), first_name)
        self.find_and_type((By.ID, "last-name"), last_name)
        self.find_and_type((By.ID, "postal-code"), postal_code)
        self.find_and_click((By.ID, "continue"))


class OverviewPage(BasePage):
    """
    Класс для страницы обзора заказа.
    Содержит методы для получения итоговой суммы и завершения покупки.
    """

    def get_total_amount(self):
        """
        Возвращает итоговую сумму заказа.
        :return: итоговая сумма в виде строки.
        """
        total_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text
        return total_text.replace("Total: $", "").strip()

    def complete_purchase(self):
        """
        Завершает процесс покупки.
        """
        self.find_and_click((By.ID, "finish"))