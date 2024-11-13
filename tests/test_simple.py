import os
from selene import browser, be, have
import time
from spinningist_project.pages.registration_page import RegistrationPage
from spinningist_project.pages.spinning_page import SpinningPage



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


def test_spinning():
    spinning_page = SpinningPage()
    spinning_page.open()
    spinning_page.spinning_section()
    spinning_page.select_spinning_brand()
    spinning_page.select_spinning_type()
    spinning_page.select_max_price()
    spinning_page.set_count_sections()
    spinning_page.click_buttom_find()
    time.sleep(4)
