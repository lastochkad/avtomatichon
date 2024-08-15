from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(
        GeckoDriverManager().install()))

try:
    driver.get("http://the-internet.herokuapp.com/login")
    sleep(1)
    input_username = driver.find_element(By.ID, "username")
    input_username.send_keys("tomsmith")
    sleep(3)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys("SuperSecretPassword!")
    sleep(2)
    press_button_login = driver.find_element(By.CLASS_NAME, "radius").click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()