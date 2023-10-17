import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
# astea pentru implicit wait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# ultimele 2 pt explicit wait
##### IMPLICIT WAIT #######
"""
Implicit wait - asteapta numarul definit de secunde inainte sa dea eroare de element not found.
Applicatiile web pot avea mai multe elemente dinamice care apar/dispar in functie de anumite actiuni ale utilizatorului
sau pot sa fie cazuri in care timpul de incarcare/randare a site-ului sunt ineficiente,iar elementul nu apare instant.
Daca driver incearca sa interactioneze cu astfel de elemente inainte ca acestea sa apara, se va returna o eroare,
iar testele vor fi marcate ca "picate" .
"""
def get_time():
    return datetime.now().strftime("%H:%M:%S")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

LINK = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"

driver.get(LINK)
# driver.implicitly_wait(20)
#
# button_change_text = driver.find_element(By.ID, "populate-text")
# button_change_text.click()
# print(f'{get_time()}: Incepem asteptarea')
# h2_text_selenium_webdriver = driver.find_element(By.XPATH, "//h2[@id='h2' and text()='Selenium Webdriver']")
# print(f'{get_time()}: S-a gasit elementul')
# # Resetam wait-ul implicit la 0 , va gasi elemenul sub o secunda.
# driver.implicitly_wait(10)
# print(f'{get_time()}: Incepem asteptarea')
# h2_text_selenium_webdriver = driver.find_element(By.XPATH, "//h2[@id='h2' and text()='Selenium Webdriver']")
# print(f'{get_time()}: S-a gasit elementul')

##### EXPLICIT WAIT #######

"""
Explicit wait face acelasi lucru ca si implicit wait, dar afecteaza un singur element.
Daca in acelasi fisier avem si implicit wait si explicit wait, atunci implicit wait va avea prioritate.

Wait-urile explicite sunt putin diferite de implicit_wait(), deoarece ele se aplica o singura data(in momentul
in care sunt apelate ca functie) existand mai multe conditii dupa care putem astepta sa fie indeplinite.

Exmple de conditii:
- prezenta elementului
- vizibilitatea elementului
- elementul sa contina un text
- atributul unui element sa existe
- etc.

Structura:
wait = WebdriverWait(driver, x) # WebdriverWait clasa care face driverul sa astepte,
                                x secundele cat sa astepte pana la indeplinrea condtiei,inainte de returnarea unei erori
wait.until(unexpected_condition) # unexpected_condition - conditia dupa care astepta sa se indeplineasca
"""
# Declaram Webelement

button_display_button = driver.find_element(By.ID, "display-other-button")
button_display_button.click()
wait = WebDriverWait(driver, 15)
print(f'{get_time()}: Incepem asteptarea')
# in codul de html exista buttonul,dar nu este vizibil
wait.until(EC.visibility_of_element_located((By.ID, "hidden"))) #avem duble ((By.ID, "hidden")) pentru il cere ca tuplu
print(f'{get_time()}: Elementul este vizibil')                    # ca sa il apelam , folosim * - DESPACHETAM

driver.find_element(By.ID, "hidden").click()

pass
