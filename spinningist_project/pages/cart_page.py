from selene import browser, have, be
from spinningist_project.data.user_info import User
from spinningist_project.pages.spinning_page import spinning_page
# from spinningist_project.data import user_info

class CartPage:

    def open(self):
        browser.open('https://spinningist.ru/members/order')

    def input_name(self, user: User):
        browser.element('[type="text"]').clear().send_keys(user.name)

    def input_email(self, user: User):
        browser.element('[type="email"]').clear().send_keys(user.email)

    def input_phone(self, user: User):
        browser.element('[name="contact"]').clear().send_keys(user.phone)

    def select_payment_type(self):
        browser.element('[id="naturalPaymentMethods"]').click()
        # browser.element('[value="paymentformstub2"]').submit()

        browser.all("[value^=paymentformstub][data-ami-payment-method='stub2']").element_by(
            have.exact_text('Банковская карта')
        ).click()

    def create_order(self, user: User):
        self.input_name(user.name)
        self.input_email(user.email)
        self.input_phone(user.phone)
        self.select_payment_type()


cart_page = CartPage()
