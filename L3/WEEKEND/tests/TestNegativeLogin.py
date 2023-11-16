import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from L3.OOPLOGIN.pages.LoginPage import Login
from L3.OOPLOGIN.pages.LoginPageObjects import LoginPageObjects


class TestNegativeLogin(unittest.TestCase, LoginPageObjects):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_invalid_login_username(self):
        login = Login(self.driver)
        login.open()
        login.execute_invalid_username_login()

        assert login.get_error_message() != super().invalid_username, "Username is not as expected"

    def test_invalid_login_password(self):
        login = Login(self.driver)
        login.open()
        login.execute_invalid_password_login()

        assert login.get_error_message() != super().invalid_password, "Password is not as expected"

    def test_invalid_login(self):
        login = Login(self.driver)
        login.open()
        login.execute_invalid_login()

        assert login.get_error_message() != super().invalid_username, "Password is not as expected"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
