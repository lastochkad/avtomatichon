from time import sleep
from lesson_6.selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

# driver.get("http://uitestingplayground.com/visibility")

# is_dispayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed
# print(is_dispayed)

# hide = driver.find_element(By.CSS_SELECTOR, "#hideButton").click()
# sleep(2)

# is_dispayed = driver.find_element(By.CSS_SELECTOR, "#transparentButton").is_displayed
# print(is_dispayed)
# sleep(2)

# driver.get("https://demoqa.com/radio-button")

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled
# print(is_enabled)

# is_enabled = driver.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled
# print(is_enabled)

# driver.quit()

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# cb = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
# is_selected = cb.is_selected
# print(is_selected)

# cb.click()

# is_selected = cb.is_selected
# print(is_selected)
# sleep(3)

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# div = driver.find_element(By.CSS_SELECTOR, "#page-footer")
# a = div.find_element(By.CSS_SELECTOR, "a")

# print(a.get_attribute("href"))

driver.get("https://the-internet.herokuapp.com/checkboxes")
divs = driver.find_elements(By.CSS_SELECTOR, "div")
# l = len(divs)
# print(l)
div = divs[5]
class_css = div.get_attribute("class")
print(class_css)