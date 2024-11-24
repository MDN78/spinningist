import os
import allure
import pytest
import requests
from selene import browser
from utilites import attach
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

@pytest.fixture()
def add_item_to_cart():
    url = "https://spinningist.ru/"
    token = os.getenv('TOKEN')
    payload = {
        'modlink': 'buy/2Fspinningi/2Fmaximus/2Fwinner-x/2Fudilische-spin-maximus-winner-x-27866',
        'itemId': '27866',
        'offset': 0,
        'catoffset': 0,
        'action': 'add',
        'qty': 1,
        'eshop_cart_simple': 1
    }
    # headers = {
    #     'cookie': f'vid=710aaba106794f1efde881f6e45f59fe; is_logged_in=1; session_={token}; user_session=o15.nickname_cookie10.test_login15.username_cookie10.test_login16.firstname_cookie4.Alex15.lastname_cookie0.9.id_cookie5.1889213.source_app_id1.07.ami_efa0.14.balance_cookie18.0%2526nbsp%253B%25D1%2580.16.eshop_cart_count1.016.eshop_cart_total18.0%2526nbsp%253B%25D1%2580.22.eshop_cart_total_plain1.0; uh_prev_mod=pages; uh_prev_url=https%3A%2F%2Fspinningist.ru%2F; uh_curr_mod=eshop_item; uh_curr_url=https%3A%2F%2Fspinningist.ru%2Fbuy%2Fspinningi%2Fmaximus%2Fwinner-x%2Fudilische-spin-maximus-winner-x-27866; is_cart_filled=1; session_=6850476613841020230918195556490; user_session=o15.nickname_cookie10.test_login15.username_cookie10.test_login16.firstname_cookie4.Alex15.lastname_cookie0.9.id_cookie5.1889213.source_app_id1.07.ami_efa0.14.balance_cookie18.0%2526nbsp%253B%25D1%2580.16.eshop_cart_count1.216.eshop_cart_total24.6%2520468%2526nbsp%253B%25D1%2580.22.eshop_cart_total_plain4.6468; uz_last_added_cart_item=%257B%2522id%2522%253A27866%252C%2522qty%2522%253A1%252C%2522price%2522%253A3234%257D; vid=710aaba106794f1efde881f6e45f59fe',
    # }
    headers = {
        'cookie': f'vid=710aaba106794f1efde881f6e45f59fe; is_logged_in=1; session_={token}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

