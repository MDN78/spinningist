import time
from selene import browser, have, be
from spinningist_project.data.user_info import User



class CartPage:

    def open(self):
        browser.open('https://spinningist.ru/members/order')

    def input_name(self, user: User):
        browser.element('[name="firstname"]').clear().send_keys(user.name)

    def input_email(self, user: User):
        browser.element('[type="email"]').clear().send_keys(user.email)

    def input_phone(self, user: User):
        browser.element('[name="contact"]').clear().send_keys(user.phone)

    def select_payment_type(self):
        browser.element('[id="naturalPaymentMethods"]').click()
        browser.all("[value^=paymentformstub][data-ami-payment-method='stub2']").element_by(
            have.exact_text('Банковская карта')
        ).click()

    def create_order(self, user: User):
        self.input_name(user)
        time.sleep(1)
        self.input_email(user)
        time.sleep(1)
        self.input_phone(user)
        self.select_payment_type()


cart_page = CartPage()
