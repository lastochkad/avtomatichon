from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

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