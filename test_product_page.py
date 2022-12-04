from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
import pytest
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_base_link}/?promo=offer{no}" if no != 7 else pytest.param("bugged_link", marks=pytest.mark.xfail(
    reason="Bug in product name")) for no in range(10)]


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_add_to_basket(product_name, product_price)


@pytest.mark.xfail(reason="Success message is presented")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="Success message is not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)


# lesson 4.3.step 10
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, product_base_link)
    product_page.open()
    product_page.go_to_shopping_cart()
    shopping_cart_page = BasketPage(browser, browser.current_url)
    shopping_cart_page.should_be_empty_shopping_cart()
    shopping_cart_page.should_be_empty_shopping_cart_message()
