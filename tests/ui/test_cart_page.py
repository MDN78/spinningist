from spinningist_project.data import user_info
import time
from spinningist_project.pages.cart_page import cart_page
from spinningist_project.pages.spinning_page import spinning_page


def test_create_order(add_item_to_cart):
    buyer = user_info.Alex
    cart_page.open()
    cart_page.create_order(buyer)
    time.sleep(5)
