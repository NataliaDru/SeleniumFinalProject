from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_btn.click()

    def should_add_to_basket(self, product_name, product_price):
        product_name_msg = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_IN_MSG)[0].text
        assert product_name == product_name_msg, \
            f"Incorrect product name (ER: {product_name}, FR: {product_name_msg})"

        product_price_msg = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_IN_MSG)[2].text
        assert product_price == product_price_msg, \
            f"Incorrect product price (ER: {product_price}, FR: {product_price_msg})"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
