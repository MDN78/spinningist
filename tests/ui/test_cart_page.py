from spinningist_project.data import user_info
from spinningist_project.pages.cart_page import cart_page
from spinningist_project.api.board_api import board_api

# def test_create_order(add_item_to_cart):
#     buyer = user_info.alex
#     cart_page.open()
#     cart_page.create_order(buyer)
#     cart_page.check_order_page()

def test_create_order():
    cart_page.open()
    token = board_api.get_auth_cookie()
    buyer = user_info.alex
    board_api.add_item_to_cart(token)
    cart_page.create_order(buyer)
    cart_page.check_order_page()