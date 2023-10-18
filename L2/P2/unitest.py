import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    LOGIN_LINK = "https://the-internet.herokuapp.com/login"
    BUTTON_LOGIN = (By.CLASS_NAME, "fa-2x")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(self.LOGIN_LINK)
        time.sleep(3)

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    # Test 1
    # - Verifica daca URL-ul paginii este corect
    def test_url(self):
        actual_url = self.driver.current_url
        assert self.LOGIN_LINK == actual_url, f"Unexpected URL, expected {self.LOGIN_LINK}, but found {actual_url}"
        # self.assertEqual(self.LOGIN_LINK, actual_url, "unexpected url")

    # Test 2
    # - Verifica daca titlul paginii apare corect
    def test_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title, "Unexpected title")

    # Test 3
    # - Verifica daca textul de pe elementul xpath=//h2 e corect
    def test_h2_text(self):
        expected_text = "Login Page"
        text_h2 = self.driver.find_element(By.XPATH, "//h2").text
        assert expected_text == text_h2, f"Invalid h2 text, expected {expected_text}, but found {text_h2}"
        # Observam ca folosind assertEqual, nu mai trebuie scrisa partea cu "expected x but found y"
        # deoarece se specifica implicit prin aceasta metoda
        self.assertEqual(expected_text, text_h2, "Textul h2 este incorect")

    # Test 4
    # - Verifica daca butonul de login este displayed
    def test_buton_login_display(self):
        login_button = self.driver.find_element(*self.BUTTON_LOGIN)
        assert login_button.is_displayed(), "Butonul de Login nu este afisat"

    # Test 5
    # - Verifica daca atributul href al linkului "Elemental Selenium" este corect
    def test_atribute_hreF(self):
        expected_url = "http://elementalselenium.com/"
        # actual_url = self.driver.find_element(By.XPATH, "//*[@id='page-footer']/div/div/a").get_property("href")
        actual_url = self.driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']").get_attribute("href")
        self.assertEqual(expected_url, actual_url, "Link-ul 'href' este incorect")

    # Test 6
    # - lasa goale user si pass
    # - click login
    # - verifica daca eroarea este afisata
    def test_blank_login(self):
        # facem click pe butonul de login fara sa completam un camp
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        eroare = self.driver.find_element(By.ID, "flash")
        assert eroare.is_displayed(), "Eroarea nu este afisata dupa logare fara Username/Password"

    # metoda ajutatoare - returneaza TRUE  daca elementul este PREZENT
    # - metoda are ca parametru variabila locator: locatorul elementului dupa care asteptam
    # - folosind driver.find_elements() putem sa ne dam seama daca un element este sau nu prezent
    # - driver.find_elements() nu da eroare daca nu gaseste un element dupa un locator dat, ci returneaza o lista goala
    # - daca lista este goala, inseamna ca nu este un element prezent [len(lista) = 0 deci return FALSE]
    # - daca lista nu este goala, inseamna ca avem cel putin un element gasit [len(lista) > 0 deci return TRUE]


    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0  # daca nu gaseste nimic returneaza o lista goala

    def test_brute_force(self):
        element_h4 = self.driver.find_element(By.XPATH, "//h4").text
        potentiale_parole = element_h4.split(" ")

        for parola in potentiale_parole:
            username = self.driver.find_element(*self.USERNAME)
            username.send_keys("tomsmith")
            password = self.driver.find_element(*self.PASSWORD)
            password.send_keys(str(parola))
            self.driver.find_element(*self.BUTTON_LOGIN).click()
            mesaj_eroare = (By.XPATH, "//div[contains(text(), 'Your password is invalid!')]")
            #  daca apare mesj de eroare cuvantul nu este corect ,inca nu am gasit parola
            #  veririficam daca msj eroare e prezent pe pagina pritn nu am gasit
            # if len(self.driver.find_elements(*mesaj_eroare)) > 0:
            if self.is_element_present(mesaj_eroare):
                print("Inca nu am gasit parola")
            else:
                print(f"Parola corecta este: '{parola}'")
                break

            # try:
            #     self.driver.find_element(*mesaj_eroare)
            #     print("Inca nu am gasit parola")
            # except NoSuchElementException:
            #     print(f"Parola corecta este: '{parola}'")
            #     break

"""
În acest context, apelul self.is_element_present(mesaj_eroare) este utilizat pentru a verifica dacă mesajul de eroare 
specificat de mesaj_eroare este prezent pe pagină. Dacă este prezent, atunci se afișează mesajul "Inca nu am gasit parola" 
pentru a indica că parola nu este corectă. 
Dacă nu este prezent, atunci se consideră că parola este corectă și se afișează mesajul "Parola corecta este: '{parola}'".
"""