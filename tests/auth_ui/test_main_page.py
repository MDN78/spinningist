from spinningist_project.pages.main_page import main_page

def test_delivery_menu():
    main_page.open()
    main_page.select_delivery_menu()
    main_page.delivery_menu_should_have_text()

def test_payment_menu():
    main_page.open()
    main_page.select_payment_menu()
    main_page.payment_block_should_have_text()
