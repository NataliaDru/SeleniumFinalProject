from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
