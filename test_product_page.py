from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{no}" if no != 7 else pytest.param("bugged_link", marks=pytest.mark.xfail(
    reason="Bug in product name")) for no in range(10)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_add_to_basket(product_name, product_price)
