import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestMultipleTabs(unittest.TestCase):
    multiple_tabs = (By.CSS_SELECTOR, "#content > ul > li:nth-child(33) > a")
    multiple_tabs_btn = (By.CSS_SELECTOR, "#content > div > a")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com")



    # def test_multiple_tabs(self):
    #     self.driver.get("https://the-internet.herokuapp.com/windows")
    #     time.sleep(3)
    #     for i in range(5):
    #         self.driver.find_element(*self.multiple_tabs_btn).click()
    #     time.sleep(5)

    def test_multiple_tabs(self):
        self.driver.find_element(*self.multiple_tabs).click()
        time.sleep(1)
        self.driver.find_element(*self.multiple_tabs_btn).click()
        time.sleep(2)
        one = self.driver.window_handles[0]
        two = self.driver.window_handles[1]
        i = 0
        while i < 100:
            self.driver.switch_to.window(one)
            self.driver.switch_to.window(two)
            i += 1
            print(i)


    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
