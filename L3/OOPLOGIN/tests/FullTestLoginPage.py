import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from L3.OOPLOGIN.pages.BasePage import BasePage
from L3.OOPLOGIN.pages.LoginPageObjects import LoginPageObjects

class LoginTest(unittest.TestCase, BasePage, LoginPageObjects):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(super().log_in_page_url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def test_login_success(self):
        driver = self.driver

        username_locator = driver.find_element(By.XPATH, super().username_field_xpath)
        password_locator = driver.find_element(By.XPATH, super().password_field_xpath)
        submit_login_locator = driver.find_element(By.XPATH, super().submit_login_button_xpath)

        # Wait for the page to load after clicking the login button
        driver.implicitly_wait(5)
        wait = self.wait
        wait.until(EC.visibility_of_element_located((By.XPATH, super().username_field_xpath)),  "Username field is not visible")
        wait.until(EC.visibility_of_element_located((By.XPATH, super().submit_login_button_xpath)),  "Logout Button is not visible")

        username_locator.send_keys(super().valid_username)
        password_locator.send_keys(super().valid_password)
        submit_login_locator.click()

        # Check if login was successfull
        actual_url = driver.current_url
        assert actual_url == super().successfully_logged_in_url, "The URL is not as expected"

        successfully_logged_in_locator = driver.find_element(By.XPATH, super().logged_in_successfully_xpath)
        log_out_button_locator = driver.find_element(By.LINK_TEXT, super().log_out_button_link)


        assert successfully_logged_in_locator.text == super().successfully_logged_in_text, "The Successfully Logged In Message is not as expected"

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, super().log_out_button_link)))
        assert log_out_button_locator.is_displayed(), "The log out button is not displayed"

    def test_login_failure(self):
        driver = self.driver

        username_locator = driver.find_element(By.XPATH, super().username_field_xpath)
        password_locator = driver.find_element(By.XPATH, super().password_field_xpath)
        submit_login_locator = driver.find_element(By.XPATH, super().submit_login_button_xpath)

        driver.implicitly_wait(5)
        wait = self.wait
        wait.until(EC.visibility_of_element_located((By.XPATH, super().username_field_xpath)))
        wait.until(EC.visibility_of_element_located((By.XPATH, super().submit_login_button_xpath)))

        username_locator.send_keys(super().invalid_username)
        password_locator.send_keys(super().valid_password)
        submit_login_locator.click()

        # Wait for the page to load after clicking the login button
        driver.implicitly_wait(5)

        # Check if the login failed
        error_message = driver.find_element(By.XPATH, super().login_data_invalid_label_xpath)
        wait.until(EC.visibility_of_element_located((By.XPATH, super().login_data_invalid_label_xpath)), "Username label not visible")
        assert error_message.text == super().username_invalid_expected_message, "The login failed message not as expected"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


