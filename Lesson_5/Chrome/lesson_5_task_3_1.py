from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

try:
    driver.get(" http://the-internet.herokuapp.com/add_remove_elements/")

    # Нажимаем на кнопку 5 раз
    for _ in range(5):
        add_button = driver.find_element(
            By.XPATH, '//button[text()="Add Element"]'
        ).click()
        sleep(2)

    # Собираем список кнопок Delete
    chrome_delete_buttons = driver.find_elements(
        "xpath", '//button[text()="Delete"]'
    )

    # Выводим резульатат на экран

    print(
        f"Размер списка кнопок Delete:{len(chrome_delete_buttons)}"
    )

except Exception as ex:
    print(ex)
finally:
    driver.quit()