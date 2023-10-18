import  time
import unittest
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class TestAltex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.emag.ro/")
        # self.driver.implicitly_wait(2)
        time.sleep(2)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


    def testTitle(self):
        actual_ = self.driver.title
        expected_ = "Electronice si electrocasnice online la cel mai mic pret"

        self.assertEqual(expected_, actual_, "Not same !")

    def test_search(self):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='search']")
        search_box.send_keys("iphone 14")
        click_search = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default searchbox-submit-button']")
        click_search.click()
        time.sleep(2)

        elements = self.driver.find_elements(By.CLASS_NAME, 'card-v2-title-wrapper')
        self.assertGreaterEqual(len(elements), 71)
