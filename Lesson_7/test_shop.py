from shop_page import LoginPage
from shop_page import ProductsPage
from shop_page import CheckoutPage
from shop_page import PersonalInfoPage
from shop_page import OverviewPage
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    """
    Фикстура для создания и закрытия экземпляра веб-драйвера.
    :return: объект веб-драйвера Selenium.
    """
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

def test_complete_purchase(browser):
    """
    Тестирует процесс покупки товаров на сайте.
    """
    login_page = LoginPage(browser)
    products_page = ProductsPage(browser)
    checkout_page = CheckoutPage(browser)
    personal_info_page = PersonalInfoPage(browser)
    overview_page = OverviewPage(browser)

    login_page.open()
    login_page.login()

    products_page.add_products_to_cart("sauce-labs-backpack", "sauce-labs-bolt-t-shirt", "sauce-labs-onesie")
    products_page.go_to_cart()

    checkout_page.proceed_to_checkout()

    personal_info_page.fill_personal_info("Alexander", "Angievskii", "74900")

    total_amount = overview_page.get_total_amount()
    assert total_amount == "58.29", f"Expected '58.29', but got {total_amount}"

    overview_page.complete_purchase()