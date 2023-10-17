import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Keys

class TestKeys(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")


    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.LINK)
        time.sleep(1)

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


    def test_keys(self):
        user = self.driver.find_element(*self.USERNAME)
        user = self.driver.find_element(*self.USERNAME)
        user.send_keys("username")
        time.sleep(2)
        user.clear()
        user.send_keys("username")
        time.sleep(1)
        user.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        user.send_keys("username")
        time.sleep(1)
        user.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        user.send_keys(Keys.SHIFT, Keys.ARROW_LEFT)
        time.sleep(1)
        user.send_keys(Keys.SHIFT, Keys.ARROW_LEFT)
        time.sleep(1)
        user.send_keys(Keys.SHIFT, Keys.ARROW_LEFT)
       


"""
Libraria keys este o librarie prin intermediul careia putem introduce o simulare a tastelor direct prin intermediul automatizarii.

Ca sa putem sa folosim aceasta librarie ne folosim de importul urmator: from selenium.webdriver.common.keys import Keys

user = self.chrome.find_element(*self.USERNAME)
user.send_keys("anton")
Acum sa presupunem ca vrem sa stergem valoarea anton si sa o inlocuim cu mariapopescu@gmail.com.
Pentru asta putem sa scriem urmatoarele comenzi:
user.send_keys(Keys.CONTROL, 'a')
user.send_keys(Keys.BACKSPACE)
user.send_keys("mariapopescu@gmail.con")

Acum poate am gresit caracterul n si vrem sa il inlocuim cu m. In cazul asta folosim urmatoarea instructiune:

user.send_keys(Keys.SHIFT, Keys.ARROW_LEFT, 'm')

Ce s-a intamplat mai sus a fost sa introducem trei  taste: valoare shift, valoarea sagetica stanga si apoi valoarea ‘m’

"""


