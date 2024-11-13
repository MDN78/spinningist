from selene import browser, be, have
import time


def test_open_page():
    browser.open('/')

    time.sleep(2)
