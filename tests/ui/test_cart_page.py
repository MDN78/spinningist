from spinningist_project.data import user_info
import time
from spinningist_project.pages.cart_page import cart_page
from spinningist_project.pages.spinning_page import spinning_page


def test_create_order():
    buyer = user_info.Alex
    cart_page.open()
    spinning_page.add_spinning_to_cart()
    cart_page.input_name(buyer)
    cart_page.input_email(buyer)
    cart_page.input_phone(buyer)
    cart_page.select_payment_type()
    time.sleep(5)