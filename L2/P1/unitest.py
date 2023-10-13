import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    LOGIN_LINK = "https://the-internet.herokuapp.com/login"

    # suprascriem ( facem override ) methoda setUp()
    # se execute inainte de fiecare test
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LOGIN_LINK)
        # self.driver.maximize_window()
        time.sleep(5)

    # suprascriem ( facem override ) metoda tearDown()
    # se executa dupa fiecare test
    def tearDown(self):
        # self.driver.close()
        self.driver.quit()

    # Test 1
    # - Verifica daca URL-ul paginii este corect
    def test_url(self):
        actual_url = self.driver.current_url

        assert self.LOGIN_LINK == actual_url, f"Unexpected URL, expected {self.LOGIN_LINK}, but found {actual_url}"
    def test_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title

        #assert expected_title == actual_title, "Unexpected title"
        self.assertEqual(expected_title, actual_title, "Unexpected title") # puteam scrie si asa 


