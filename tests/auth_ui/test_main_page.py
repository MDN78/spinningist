from spinningist_project.pages.main_page import main_page

def test_delivery_menu():
    main_page.open()
    main_page.select_delivery_menu()
    main_page.main_page_should_have_text()