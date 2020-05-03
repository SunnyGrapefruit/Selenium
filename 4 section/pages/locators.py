from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTER_USER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_USER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_USER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_USER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-primary")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    BOOK_TITLE = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    ASSERT_BOOK_TITLE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) div.alertinner strong")
    ASSERT_BOOK_PRICE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_CART = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators():
    EMPTY_CART = (By.XPATH, "//*[@id='content_inner']/p")
    ITEMS_IN_CART = (By.CLASS_NAME, "basket-title")
