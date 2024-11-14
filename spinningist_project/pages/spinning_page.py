from utilites.logger import Logger

from selenium.webdriver import ActionChains, Keys
from selene import browser, have, be
from selene.core import command

from utilites.logger import Logger


class SpinningPage:

    def open(self):
        browser.open('https://spinningist.ru')

    def spinning_section(self):
        browser.element('[class="b-menu__item"]').click()

    def select_spinning_brand(self):
        browser.element('[id="checkbox_spec_eshop_filter_001003112ext_custom_13[]_11"]').click()

    def select_spinning_class(self):
        browser.element('[id="checkbox_spec_eshop_filter_001003112ext_custom_75[]_5"]').click()

    def select_spinning_type(self):
        browser.element('[id="checkbox_spec_eshop_filter_001003112ext_custom_96[]_1"]').click()

    def select_max_price(self):
        # price = browser.element('[class="cmallFilter__rangeSlider_price_to form-control b-cmall-eshop-filter-spec-cf__item-text b-cmall-eshop-filter-spec-cf__item-text-to"]').send_keys(Keys.BACKSPACE * 6)
        # price.send_keys('12000')
        browser.element(
            '[class="cmallFilter__rangeSlider_price_to form-control b-cmall-eshop-filter-spec-cf__item-text b-cmall-eshop-filter-spec-cf__item-text-to"]').perform(
            command.js.set_value('12000')).click()

    def set_count_sections(self):
        browser.element('[id="checkbox_spec_eshop_filter_001003112ext_custom_77[]_3"]').click()

    def click_buttom_find(self):
        browser.element('[class="btn btn-black b-cmall-filter_form-field_submit__next-btn"]').click()

    def page_should_have_text(self):
        browser.element('[class="eshop-item-list__search-result 123"]').should(have.text('Найдено товаров'))

    def select_spinning(self):
        browser.element('[title="Удилище спин. Maximus Winner-X 24L 2,4m 3-15g"]').click()

    def should_have_text_selected_spinning(self):
        browser.element('[class="b-cmall-eshop-itemD-detail__item-name"]').should(
            have.text('Удилище спин. Maximus Winner-X 24L 2,4m 3-15g'))


    def add_to_cart(self):
        browser.element('[class="fa fa-shopping-cart eshop-item-small__cart-text"]').click()

    def got_to_cart(self):
        browser.element('[class="btn btn-primary modal-cart-order-btn b-cmall-eshop-cart-added-modal__footer-button-order"]').click()

    def should_have_text_cart(self):
        browser.element('[class="b-cmall-page-name__order"]').should(have.text('Оформление заказа'))


    def choose_spinning(self):
        Logger.add_start_step(method='select_spinning')
        self.spinning_section()
        self.select_spinning_brand()
        self.select_spinning_class()
        self.select_spinning_type()
        self.select_max_price()
        self.set_count_sections()
        self.click_buttom_find()
        self.page_should_have_text()
        self.select_spinning()
        Logger.add_end_step(url=browser.driver.current_url, method='select_spinning')

    def add_spinning_to_cart(self):
        Logger.add_start_step(method='add spinning to cart')
        self.choose_spinning()
        self.add_to_cart()
        self.got_to_cart()
        Logger.add_end_step(url=browser.driver.current_url, method='add spinning to cart')


spinning_page = SpinningPage()
