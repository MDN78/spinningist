from selene import browser, be, have
import time
from spinningist_project.pages.registration_page import RegistrationPage


def test_open_page():
    browser.open('/')
    browser.element('[class="hidden-sm hidden-xs b-cmall-members-small_menu_login__item-link-name"]').click()

    time.sleep(2)


def test_login():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_login('test_login')
    registration_page.fill_password('111111test')
    registration_page.submit()
