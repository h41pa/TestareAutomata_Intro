from selenium.webdriver.common.by import By

from L3.OOPLOGIN.pages.BasePage import BasePage
from L3.OOPLOGIN.pages.LoginPageObjects import LoginPageObjects


class LoggedInSuccessfully(BasePage, LoginPageObjects):
    def __init__(self, driver):
        super().__init__(driver)

    def get_expected_url(self):
        return super().successfully_logged_in_url

    def get_header_message(self):
        header_locator = (By.XPATH, super().logged_in_successfully_xpath)
        return super().get_text(header_locator)

    def is_logout_button_displayed(self):
        logout_button_locator = (By.LINK_TEXT, super().log_out_button_link)
        return super().is_displayed(logout_button_locator)