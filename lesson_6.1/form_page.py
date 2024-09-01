"""
Модуль для тестирования формы с полями с использованием Selenium и pytest.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
class FormPage:
    """
    Класс, представляющий страницу с формой.
    """
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.form_fields = {
            "first_name": (By.CSS_SELECTOR, "input[type='text'][name='first-name']"),
            "last_name": (By.CSS_SELECTOR, "input[type='text'][name='last-name']"),
            "address": (By.CSS_SELECTOR, "input[type='text'][name='address']"),
            "zip_code": (By.CSS_SELECTOR, "input[type='text'][name='zip-code']"),
            "city": (By.CSS_SELECTOR, "input[type='text'][name='city']"),
            "country": (By.CSS_SELECTOR, "input[type='text'][name='country']"),
            "email": (By.CSS_SELECTOR, "input[type='email'][name='e-mail']"),
            "phone": (By.CSS_SELECTOR, "input[type='text'][name='phone']"),
            "job_position": (By.CSS_SELECTOR, "input[type='text'][name='job-position']"),
            "company": (By.CSS_SELECTOR, "input[type='text'][name='company']"),
        }
        self.submit_button = (By.XPATH, "//button[@type='submit']")
        self.zip_code_alert = (By.ID, "zip-code")
    def open_page(self, url):
        """Открыть веб-страницу с указанным URL."""
        self.driver.get(url)
        
    def fill_form(self, field_name, value):
        """
        Заполнить указанное поле формы переданным значением.
        Args:
            field_name (str): Имя поля формы.
            value (str): Значение для ввода в поле формы.
        """
        field_locator = self.form_fields.get(field_name.lower()) # First_Name first_name
        if field_locator:
            self.wait.until(EC.visibility_of_element_located(field_locator)).send_keys(value)

    def scroll_form(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")




    def submit_form(self):
        """Отправить форму на веб-странице."""
        submit_button = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        submit_button.click()
    def get_zip_code_highlight_color(self):
        """Получить цвет фона для предупреждения zip-code."""
        zip_code_alert = self.wait.until(EC.visibility_of_element_located(self.zip_code_alert))
        return zip_code_alert.value_of_css_property("background-color")
    def get_field_highlight_color(self, field_id):
        """Получить цвет фона для указанного поля формы."""
        field_locator = (By.CSS_SELECTOR, f"div.alert.py-2.alert-success#{field_id}")
        field = self.wait.until(EC.visibility_of_element_located(field_locator))
        return field.value_of_css_property("background-color")