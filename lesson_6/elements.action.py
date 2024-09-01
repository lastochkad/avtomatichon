from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

driver.get("https://ya.ru")

txt = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').text
print(txt)
tag = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').tag_name
print(tag)
id = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').id
print(id)
href = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').get_attribute("href")
print(href)

css = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').value_of_css_property("font-family")
print(css)
color = driver.find_element(By.CSS_SELECTOR, 'a[data-statlog="2informers.stocks.item.1"]').value_of_css_property("color")
print(color)

sleep(10)
driver.quit()