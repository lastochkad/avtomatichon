from time import sleep
from lesson_6.selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

driver.get("https://demoqa.com/browser-windows")
c = driver.find_element(By.ID, "#tabButton").click()

# # driver.close()
# sleep(10)
# driver.quit()