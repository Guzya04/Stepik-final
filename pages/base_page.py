from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class BasePage:
    def __init__(self, browser: RemoteWebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
