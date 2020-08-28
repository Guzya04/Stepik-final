from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button.btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main h1")
    AMOUNT_OF_PRODUCT = (By.CSS_SELECTOR, "#content_inner .product_main .price_color")
    ALERT_SUCCESS_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > :nth-child(1) .alertinner strong")
    ALERT_SUCCESS_BASKET_AMOUNT = (By.CSS_SELECTOR, "#messages > :nth-child(3) .alertinner strong")
