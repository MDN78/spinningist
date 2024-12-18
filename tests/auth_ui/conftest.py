import os
import allure
import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from utilites import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def driver_configuration():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://spinningist.ru"

    yield

    with allure.step('Add screenshot'):
        attach.add_screenshot(browser)

    with allure.step('Add logs'):
        attach.add_logs(browser)

    with allure.step('Add html'):
        attach.add_html(browser)
    #
    # with allure.step('Add video'):
    #     attach.add_video(browser)

    with allure.step('Close driver'):
        browser.quit()
