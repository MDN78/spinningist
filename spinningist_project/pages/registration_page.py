from selene import browser, have, be

class RegistrationPage():

    def open(self):
        browser.open('https://spinningist.ru/members')

    def fill_login(self, value):
        browser.element('[name="username"]').should(be.blank).send_keys(value)

    def fill_password(self, value):
        browser.element('[name="password"]').should(be.blank).send_keys(value)

    def submit(self):
        browser.element('[class="btn btn-black pull-right"]').click()