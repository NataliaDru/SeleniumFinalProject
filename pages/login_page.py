from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Where is no Login page or URL doesn't contain 'login'"
        # assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), \
            "Registration form is not presented"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD1)
        reg_pass1.send_keys(password)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2)
        reg_pass2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()
