from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD1 = (By.ID, "id_registration-password1")
    REG_PASSWORD2 = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")


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
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, '[href$="basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    SHOPPING_CART_STATUS = (By.CSS_SELECTOR, '#content_inner p')
    LANGUAGE = (By.CSS_SELECTOR, "#content_inner a")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
