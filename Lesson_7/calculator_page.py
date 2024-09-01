"""
Этот модуль содержит тест для веб-приложения калькулятора
с использованием Selenium WebDriver и pytest.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class CalculatorPage:
    """
    Класс Page Object для страницы медленного калькулятора.
    Содержит методы для взаимодействия с элементами интерфейса калькулятора.
    """

    def __init__(self, driver):
        """
        Инициализирует экземпляр CalculatorPage с экземпляром WebDriver.
        :param driver: Экземпляр WebDriver для взаимодействия с браузером
        """
        self.driver = driver

    def open_page(self, url):
        """
        Открывает страницу калькулятора по указанному URL.
        :param url: URL страницы калькулятора
        """
        self.driver.get(url)

    def enter_delay_value(self, delay_value):
        """
        Вводит значение задержки в поле ввода.
        :param delay_value: Строковое значение задержки
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay_value)

    def click_button(self, button_text):
        """
        Нажимает на кнопку калькулятора с указанным текстом.
        :param button_text: Текст на кнопке, которую нужно нажать
        """
        button_locator = (
            f"//span[contains(@class, 'btn-outline-primary') and text()='{button_text}']"
        )
        button = self.driver.find_element(By.XPATH, button_locator)
        button.click()

    def click_operator_button(self, operator):
        """
        Нажимает на кнопку оператора на калькуляторе.
        :param operator: Оператор, на который нужно нажать (например, '+', '-', '*', '/')
        """
        operator_locator = (
            f"//span[contains(@class, 'operator') and text()='{operator}']"
        )
        operator_button = self.driver.find_element(By.XPATH, operator_locator)
        operator_button.click()

    def click_equals_button(self):
        """
        Нажимает на кнопку равно на калькуляторе.
        """
        equals_locator = "//span[contains(@class, 'btn-outline-warning') and text()='=']"
        equals_button = self.driver.find_element(By.XPATH, equals_locator)
        equals_button.click()

    def get_result_text(self):
        """
        Возвращает текст, отображаемый на экране калькулятора.
        :return: Текст, отображаемый на экране, в виде строки
        """
        result_element = WebDriverWait(self.driver, 45).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen"))
        )
        return result_element.text