import time
from spinningist_project.pages.spinning_page import SpinningPage


def test_spinning():
    spinning_page = SpinningPage()
    spinning_page.open()
    spinning_page.spinning_section()
    spinning_page.select_spinning_brand()
    spinning_page.select_spinning_class()
    spinning_page.select_spinning_type()
    spinning_page.select_max_price()
    spinning_page.set_count_sections()
    spinning_page.click_buttom_find()
    spinning_page.page_should_have_text()
    spinning_page.select_spinning()
    spinning_page.should_have_text_selected_spinning()
    time.sleep(4)
