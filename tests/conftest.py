from pickle import FALSE
from selenium import webdriver
from dotenv import load_dotenv
import allure
import os
import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

# @pytest.fixture(scope="function", autouse=False)
# def driver_configuration():
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     browser.config.base_url = "https://spinningist.ru"
#     yield
#     browser.quit()

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
