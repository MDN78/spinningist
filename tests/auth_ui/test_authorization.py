import os
import allure
from spinningist_project.pages.registration_page import registration_page


@allure.tag('Spinningist')
def test_authorization_registered_user():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    registration_page.open()
    registration_page.registration(login, password)
    registration_page.should_have_registered_user()


def test_authorization_unregistered_user():
    login = os.getenv('UNREGISTERED_LOGIN')
    password = os.getenv('UNREGISTERED_PASSWORD')
    registration_page.open()
    registration_page.registration(login, password)
    registration_page.should_have_text_unregistered_user()
