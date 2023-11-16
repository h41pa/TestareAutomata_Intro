from selenium.webdriver.common.by import By

from L3.OOPLOGIN.pages.BasePage import BasePage
from L3.OOPLOGIN.pages.LoginPageObjects import LoginPageObjects


class Login(BasePage, LoginPageObjects):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        return super().open_url(super().log_in_page_url)

    def execute_valid_login(self):
        username_locator = (By.XPATH, super().username_field_xpath)
        password_locator = (By.XPATH, super().password_field_xpath)
        submit_locator = (By.XPATH, super().submit_login_button_xpath)
        # can write using self.type asl as long is any method type in current file
        # self.type(username_locator, self.valid_username)
        super().type(username_locator, super().valid_username)
        super().type(password_locator, super().valid_password)
        super().click(submit_locator)

    def execute_invalid_username_login(self):
        username_locator = (By.XPATH, super().username_field_xpath)
        password_locator = (By.XPATH, super().password_field_xpath)
        submit_locator = (By.XPATH, super().submit_login_button_xpath)
        super().type(username_locator, super().invalid_username)
        super().type(password_locator, super().valid_password)
        super().click(submit_locator)

    def execute_invalid_password_login(self):
        username_locator = (By.XPATH, super().username_field_xpath)
        password_locator = (By.XPATH, super().password_field_xpath)
        submit_locator = (By.XPATH, super().submit_login_button_xpath)
        super().type(username_locator, super().valid_username)
        super().type(password_locator, super().invalid_password)
        super().click(submit_locator)

    def execute_invalid_login(self):
        username_locator = (By.XPATH, super().username_field_xpath)
        password_locator = (By.XPATH, super().password_field_xpath)
        submit_locator = (By.XPATH, super().submit_login_button_xpath)
        super().type(username_locator, super().invalid_username)
        super().type(password_locator, super().invalid_password)
        super().click(submit_locator)

    def get_error_message(self):
        error_message_locator = (By.XPATH, super().login_data_invalid_label_xpath)
        return super().get_text(error_message_locator)