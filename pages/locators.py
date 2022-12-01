from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main >h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME_IN_MSG = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE_IN_MSG = (By.CSS_SELECTOR, "#messages .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
