from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def make_scrennshot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(5)
    browser.save_screenshot('./ya_'+browser.name+'.png')

chrome = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()))

FF = webdriver.Firefox(
    service=FirefoxService(
        GeckoDriverManager().install()))

make_scrennshot(chrome)
make_scrennshot(FF)