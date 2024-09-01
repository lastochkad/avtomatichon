from time import sleep
from lesson_6.selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

driver.get("https://rzd.ru")

current_title = driver.title

print(current_title)

driver.quit