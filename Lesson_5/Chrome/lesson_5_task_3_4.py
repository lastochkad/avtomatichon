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

try:
    driver.get(" http://the-internet.herokuapp.com/entry_ad")
    # Ждем пока окно не появится
    wait = WebDriverWait(driver, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal"))
    )
    close_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer"))
    )
    sleep(3)
    # Нажимаем кнопку close

    close_button.click()
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()