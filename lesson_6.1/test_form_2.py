import pytest
from form_page import FormPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture
def driver_setup():
    """
    Фикстура для настройки тестовой среды.
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.fullscreen_window()
    wait = WebDriverWait(driver, 10)
    page = FormPage(driver, wait)
    yield page
    driver.quit()
def test_fill_form_and_verify_highlight(driver_setup):
    """
    Тест для заполнения формы и проверки выделения полей.
    """
    # Шаг 1: Открытие страницы с формой
    driver_setup.open_page("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Шаги 2-11: Заполнение формы
    driver_setup.fill_form("first_name", "Иван")
    driver_setup.fill_form("last_name", "Петров")
    driver_setup.fill_form("address", "Ленина, 55-3")
    driver_setup.fill_form("zip_code", "")
    driver_setup.fill_form("city", "Москва")
    driver_setup.fill_form("country", "Россия")
    driver_setup.fill_form("email", "test@skypro.com")
    driver_setup.fill_form("phone", "+7985899998787")
    driver_setup.fill_form("job_position", "QA")
    driver_setup.fill_form("company", "SkyPro")

    driver_setup.scroll_form()


    # Шаг 12: Нажатие на кнопку Submit
    driver_setup.submit_form()

    # Шаг 13: Проверка выделения полей
    assert driver_setup.get_zip_code_highlight_color() == 'rgb(248, 215, 218)'
    fields = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
    for field in fields:
        assert driver_setup.get_field_highlight_color(field) == 'rgb(209, 231, 221)'