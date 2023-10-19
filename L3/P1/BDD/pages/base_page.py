from selenium.webdriver.common.by import By
from L3.P1.BDD.driver import Driver

class BasePage(Driver):
    SEARCH_INPUT = (By.ID, "small-searchterms")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click() # am creat metoda click folosing metoda find de mai sus

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()







