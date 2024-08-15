from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(
        GeckoDriverManager().install()))

try:
    count = 0
    driver.get(" http://uitestingplayground.com/dynamicid")

    # Нажиммаем на синюю кнопку 1 раз
    blue_button = driver.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]'
    ).click()
    # Кликаем на синюю кнопку 3 раза
    for _ in range(3):
        blue_button = driver.find_element(
            By.XPATH, '//button[text()="Button with Dynamic ID"]'
        ).click()
        count = count + 1
        sleep(2)
        print(count)

except Exception as ex:
    print(ex)
finally:
    driver.quit()