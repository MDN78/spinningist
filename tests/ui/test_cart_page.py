from spinningist_project.data import user_info
from spinningist_project.pages.cart_page import cart_page


def test_create_order(add_item_to_cart):
    buyer = user_info.alex
    cart_page.open()
    cart_page.create_order(buyer)
    cart_page.check_order_page()

