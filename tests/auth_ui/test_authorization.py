import os
from spinningist_project.pages.registration_page import RegistrationPage


def test_auth():
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.registration(login, password)
    registration_page.should_have_registered_user()


# def test_login():
#     registration_page = RegistrationPage()
#     registration_page.open()
#     login = os.getenv('LOGIN')
#     password = os.getenv('PASSWORD')
#     registration_page.fill_login(login)
#     registration_page.fill_password(password)
#     registration_page.submit()
#     time.sleep(3)