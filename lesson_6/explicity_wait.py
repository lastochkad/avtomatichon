from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 40)
driver.get("http://uitestingplayground.com/progressbar")

start = driver.find_element(By.CSS_SELECTOR, "#startButton").click()

waiter.until(
    EC.text_to_be_present_in_element(By.CSS_SELECTOR, 'aria-valuenow="75"' )
)
driver.find_element(By.CSS_SELECTOR, "#stopButton").click()

result = driver.find_element(By.CSS_SELECTOR, "#result").text

print(result)