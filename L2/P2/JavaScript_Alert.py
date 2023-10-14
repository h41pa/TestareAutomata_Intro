import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAlerts(TestCase):
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"

    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.LINK)
        time.sleep(2)

    # suprascriem metoda triedDown care va rula dupa fiecare test
    def tearDown(self):
        self.driver.quit()
