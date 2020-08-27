from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(self.timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
