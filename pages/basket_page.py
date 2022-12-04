from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_shopping_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Shopping cart is not empty"

    def should_be_empty_shopping_cart_message(self):
        basket_status = self.browser.find_element(*BasketPageLocators.SHOPPING_CART_STATUS).text
        basket_status = basket_status.split(".")[0]
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida",
            "cs": "Váš košík je prázdný",
            "da": "Din indkøbskurv er tom",
            "de": "Ihr Warenkorb ist leer",
            "en": "Your basket is empty",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide",
            "it": "Il tuo carrello è vuoto",
            "ko": "장바구니가 비었습니다",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty",
            "pt": "O carrinho está vazio",
            "pt-br": "Sua cesta está vazia",
            "ro": "Cosul tau este gol",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий",
            "zh-cn": "Your basket is empty",
        }
        assert languages[language] in basket_status, "Shopping cart is not empty or incorrect error message"
