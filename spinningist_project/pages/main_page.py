from selene import browser, have, be


class MainPage:

    def open(self):
        browser.open('https://spinningist.ru')

    def select_delivery_menu(self):
        browser.element('[class="nav-menu__item"]').click()

    def main_page_should_have_text(self):
        browser.element('[class="b-cmall-page-name text-left"]').should(have.text('ДОСТАВКА'))

main_page = MainPage()