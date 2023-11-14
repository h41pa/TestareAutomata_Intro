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

        # assert expected_title == actual_title, "Unexpected title"
        self.assertEqual(expected_title, actual_title, "Unexpected title")  # puteam scrie si asa


"""
Libraria unittest este o librarie care suporta crearea de teste  rulabile direct in interiorul clasei
Pentru a putea sa ne folosim de libraria unit test, trebuie sa cream o clasa de teste care sa mosteneasca 
clasa TestCase din libraria unittest. 
Exemplu : class TestAlerts(unittest.TestCase):
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati:

1. metoda setUp() -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva

2. metoda tearDown() -> toate activitatile care trebuie sa fie executate dupa de ORICE TEST din clasa respectiva

3. toate metodele de test trebuie sa aiba prefixul test_

In general fiecare clasa de test trebuie sa contina metode de test inrudite (adica care acopera aceeasi zona din aplicatie) si care in general sunt conditionate de acelasi set de preconditii (ex: toate testele de login trebuie sa porneasca de pe pagina de login, toate testele de search product pleaca de la actiunea initiala de cautare a unui produs etc).

Atunci cand vrem sa rulam testele putem sa o facem sub mai multe forme: 

Click pe triunghiul verde de langa numele clasei de test -> va rula toate testele din acea clasa
Click pe triunghiul verde de langa numele metodei de test -> va executa doar metoda de test pe care am rulat-o
Rularea din terminal a unui fisier de teste specific: python -m unittest filename.py
Rularea din terminal a tuturor fisierelor de test: python -m unittest

Atunci cand vrem sa sarim unele teste la rulare ne putem folosi de decoratorul @unittest.skip 
plasat inaintea fiecarei metode de test care se doreste a fi sarita.


"""
