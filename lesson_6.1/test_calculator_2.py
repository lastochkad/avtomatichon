from calculator_page import CalculatorPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def browser():
    """
    Pytest фикстура для инициализации и завершения работы WebDriver.

    :yield: Экземпляр WebDriver для использования в тестах
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator(browser):
    """
    Тест для медленного калькулятора: выполняет простую операцию сложения
    и проверяет результат.

    :param browser: Экземпляр WebDriver, предоставляемый фикстурой
    """
    calculator_page = CalculatorPage(browser)
    calculator_page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page.enter_delay_value("45")
    calculator_page.click_button("7")
    calculator_page.click_operator_button("+")
    calculator_page.click_button("8")
    calculator_page.click_equals_button()

    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    result_element = browser.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()

    print(f"Результат, отображаемый на экране: {result}")

    assert result == "15", f"Ожидаемый результат 15, но получен {result}"

if __name__ == "__main__":
    pytest.main()