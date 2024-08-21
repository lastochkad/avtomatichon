from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/textinput?")

input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_field.send_keys("SkyPro")

confirm_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
driver.implicitly_wait(5)

new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
driver.implicitly_wait(5)
print(new_button)

driver.quit()
# waiter = WebDriverWait(driver, 10)


# input = waiter.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
# )
# input.send_keys("SkyPro")


# waiter.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#updatingButton"))
# ).click()
# driver.implicitly_wait(5)

# txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
# driver.implicitly_wait(5)

# print(txt)

# driver.quit()

# input.clear()


# input.send_keys("SkyPro")
# waiter.until(
#     EC.text_to_be_present_in_element(By.CSS_SELECTOR, "#newButtonName"),"SkyPro"
# )



# driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()



# txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# print(txt)