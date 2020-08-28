from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not found in current url."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found."

    def register_new_user(self, email: str, password: str):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_REGISTER).click()
