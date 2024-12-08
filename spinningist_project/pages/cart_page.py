import time
from selene import browser, have, be
from spinningist_project.data.user_info import User
from selene.core import command


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

    def selec_delivery_type(self):
        browser.element('[id="shipping_method_11_11"]').perform(command.js.click)

    def turn_of_policy(self):
        browser.element('[id="order_agreement_checkbox"]').click()

    def check_order_page(self):
        browser.element('[class="eshop-ordering__submit eshop-ordering__submit_action_order btn eshop-ordering__submit_orig"]').should(be.hidden)

    def create_order(self, user: User):
        self.input_name(user)
        self.input_email(user)
        self.input_phone(user)
        self.select_payment_type()
        self.selec_delivery_type()
        self.turn_of_policy()


cart_page = CartPage()
