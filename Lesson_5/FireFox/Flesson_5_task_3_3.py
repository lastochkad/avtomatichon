from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(
        GeckoDriverManager().install()))

try:
    driver.get("http://uitestingplayground.com/classattr")

    # Запускаем скрипт 3 раза
    for x in range(3):
        # Кликаем на синюю кнопку
        blue_button = driver.find_element(
            By.CSS_SELECTOR, "button.btn-primary"
        ).click()
        sleep(2)
    # Кликаем на ОК в модальном окне
        driver.switch_to.alert.accept()

except Exception as ex:
    print(ex)
finally:
    driver.quit()