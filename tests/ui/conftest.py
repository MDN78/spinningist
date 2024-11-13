import os
import pytest
import allure
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def auth_driver_configuration():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://spinningist.ru"
    token = os.getenv('TOKEN')
    cookie = {
        "name": "session_",
        "value": token
    }
    browser.open('/')
    browser.driver.add_cookie(cookie)

    yield

    browser.quit()
