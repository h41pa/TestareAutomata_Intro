from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ElefantTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.elefant.ro/")
        self.driver.implicitly_wait(2)
        sleep(6)

    def tearDown(self):
        sleep(1)
        self.driver.quit()
    # - Test 1: Intrati pe site-ul https://www.elefant.ro/

    # metoda care se ruleaza la inceputul oricarui Test Case (scenariu de test)
    def test_open_site(self):
        sleep(2)

# - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
    def test_search_product(self):
        # search field
        search_field = self.driver.find_element(By.XPATH, "//input[@name='SearchTerm'][@class='form-control searchTerm js-has-overlay']")

        # send text to field
        search_field.send_keys("iphone 14")
        sleep(2)

        # click search button
        search_button = self.driver.find_element(By.XPATH, "//button[@class='btn-search btn btn-primary'][@name='search']")
        search_button.click()
        sleep(4)
        # extract products

        products = self.driver.find_elements(By.CLASS_NAME, "product-title")
        self.assertGreaterEqual(len(products), 10)
