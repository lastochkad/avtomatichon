from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

try:
    driver.get(" http://the-internet.herokuapp.com/inputs")
    input_pole = driver.find_element(By.TAG_NAME, "input")
    input_pole.send_keys("1000")
    sleep(2)
    input_pole.clear()
    sleep(1)
    input_pole.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()