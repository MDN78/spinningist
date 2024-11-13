from selenium.webdriver import ActionChains, Keys
from selene import browser, have, be
from selene.core import command


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
        browser.element('[class="cmallFilter__rangeSlider_price_to form-control b-cmall-eshop-filter-spec-cf__item-text b-cmall-eshop-filter-spec-cf__item-text-to"]').perform(command.js.set_value('12000'))

    def set_count_sections(self):
        browser.element('[id="checkbox_spec_eshop_filter_001003112ext_custom_77[]_3"]').click()

    def click_buttom_find(self):
        browser.element('[class="btn btn-black b-cmall-filter_form-field_submit__next-btn"]').click()