from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE_MAIN = (By.CSS_SELECTOR, "div.message-error")
    ERROR_MESSAGE_EMAIL = (By.ID, "Email-error")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.type(self.EMAIL_INPUT, email)  # nu mai despachetam cu * pt e despachetat in base_page in metoda find

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        # self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.click(self.LOGIN_BUTTON)
