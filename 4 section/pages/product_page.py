from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):

    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        add_button.click()

    def assert_add_to_cart(self):
        # time.sleep(5)
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert_book_title = self.browser.find_element(*ProductPageLocators.ASSERT_BOOK_TITLE).text
        assert_book_price = self.browser.find_element(*ProductPageLocators.ASSERT_BOOK_PRICE).text
        assert book_title == assert_book_title, "Название не соответсвует"
        assert book_price == assert_book_price, ("Цена не соответствует", book_price, assert_book_price)


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"