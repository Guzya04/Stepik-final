from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_different_positions_count(self):
        return len(self.browser.find_elements(*BasketPageLocators.BASKET_CONTENT))

    def basket_should_contains_n_different_position(self, n: int = 0):
        count_different_positions = self.basket_different_positions_count()
        assert count_different_positions == n, f"Count of different positions in basket is " \
                                               f"{count_different_positions}, but should be {n}"

    def should_be_text_about_empty_basket(self):
        # TODO: Сделать проверку для разных языков
        assert self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTY).text is not None, "Should be text " \
                                                                                                 "about empty basket"
