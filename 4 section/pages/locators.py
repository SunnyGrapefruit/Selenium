from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-primary")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BOOK_TITLE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    ASSERT_BOOK_TITLE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ASSERT_BOOK_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")