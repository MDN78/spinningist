import time
from spinningist_project.pages.spinning_page import spinning_page


def test_spinning():
    spinning_page.open()
    spinning_page.choose_spinning()
    spinning_page.should_have_text_selected_spinning()

