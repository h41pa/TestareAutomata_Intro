from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator: tuple):
        # find element requires 2 parameters, by and value
        # we use * to send multiple param to locator
        # * always sends param as tuple
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, message: str, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).send_keys(message)

    def get_text(self, locator, time=10):
        self.wait_for_visible_element(locator, time)
        return self.find(locator).text

    def click(self, locator: tuple, time: int = 10):
        self.wait_for_visible_element(locator, time)
        self.find(locator).click()

    def is_displayed(self, locator: tuple):
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def wait_for_visible_element(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.visibility_of_element_located(locator), "Element not visible")

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url: str):
        self.driver.get(url)
