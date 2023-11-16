import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from L3.OOPLOGIN.pages.LoggedInSuccessfullyPage import LoggedInSuccessfully
from L3.OOPLOGIN.pages.LoginPage import Login
from L3.OOPLOGIN.pages.LoginPageObjects import LoginPageObjects


class TestPositiveLogin(unittest.TestCase, LoginPageObjects):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_positive_login(self):

        login = Login(self.driver)
        login.open()
        login.execute_valid_login()

        logged_in = LoggedInSuccessfully(self.driver)
        assert logged_in.get_expected_url() == logged_in.get_current_url(), "Acutal URL is not the same as expected"
        assert logged_in.get_header_message() == super().successfully_logged_in_text, "Header message not as expected"
        assert logged_in.is_logout_button_displayed(),  "Logout button should be visible"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
