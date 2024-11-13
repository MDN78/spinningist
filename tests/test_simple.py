import os

from selene import browser, be, have
import time
from spinningist_project.pages.registration_page import RegistrationPage


def test_open_page():
    browser.open('/')
    # browser.element('[class="hidden-sm hidden-xs b-cmall-members-small_menu_login__item-link-name"]').click()

    time.sleep(2)


def test_login():
    registration_page = RegistrationPage()
    registration_page.open()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    registration_page.fill_login(login)
    registration_page.fill_password(password)
    registration_page.submit()
    time.sleep(3)


