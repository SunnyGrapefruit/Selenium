from .base_page import BasePage
from .locators import CartPageLocators
from .locators import ProductPageLocators

class BasketPage(BasePage):
    def no_item_in_cart(self): #Ожидаем, что в корзине нет товаров
        assert self.item_in_cart(*CartPageLocators.ITEMS_IN_CART), "В корзине оказались товары"

    def message_that_cart_is_empty(self): #Ожидаем, что есть текст о том что корзина пуста
        assert self.cart_is_empty(*CartPageLocators.EMPTY_CART), "Нет сообщения что корзина пуста"


    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        add_button.click()