from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class ProductPage(BasePage):
    def __init__(self, browser: RemoteWebDriver, url: str):
        super().__init__(browser, url)
        self.button_add_to_basket = None
        self.name_of_product = None
        self.amount_of_product = None

    def open(self):
        super().open()
        self.button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        self.name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        self.amount_of_product = self.browser.find_element(*ProductPageLocators.AMOUNT_OF_PRODUCT).text.replace("£", "")

    def click_button_add_to_basket(self):
        self.button_add_to_basket.click()

    def should_check_adding_product_to_basket(self):
        self.should_check_correct_product_name_added()
        self.should_check_basket_amount()

    def should_check_correct_product_name_added(self):
        text = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_NAME_PRODUCT).text
        assert self.name_of_product in text, \
            f"In first alert success '{text}' not a name of product - '{self.name_of_product}'"

    def should_check_basket_amount(self):
        text = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_BASKET_AMOUNT).text
        assert self.amount_of_product in text, \
            f"In third alert success (basket) '{text}' not a amount of product - '{self.amount_of_product}'"

