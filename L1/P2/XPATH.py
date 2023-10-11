"""


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/form"

driver.get(LINK)

# Cauta primul element de tip input
driver.find_element(By.XPATH, "(//input)[1]")

# Cauta al doilea element de tip input
driver.find_element(By.XPATH, "(//input)[2]")

# Al doilea copil cu tag-ul <div> al unui element parinte oarecare - se observa ca parintele nu este specificat
driver.find_element(By.XPATH, "//div[2]")

# Al doilea copil cu tag-ul ORICARE * al unui element parinte oarecare, cu clasa 'form-control'
driver.find_element(By.XPATH, "//*[2][@class='form-control']")

# Primul element copil cu tag-ul <input> cu id='last-name' al unui parinte <div>
driver.find_element(By.XPATH, "//div/input[1][@id='last-name']")

# Ultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()]")

# Penultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()-1]")

# Simbolul | (pipe) - se foloseste intre 2 XPATH-uri ---
# Simbolul | (pipe) - sau logic
# input cu id=id-inexistent sau input cu id=first-name
driver.find_element(By.XPATH, "//input[@id='id-inexistent'] | //input[@id='first-name']")

# Simbolul or - se foloseste intre 2 attribute ---
# Simbolul or - sau logic
# input cu id=first sau id=last
driver.find_element(By.XPATH, "//input[contains(@id,'first') or contains(@id,'last')]")

# Simbolul and - se foloseste intre 2 atribute
# Simbolul and - si logic
# input cu id=frist si id=name
driver.find_element(By.XPATH, "//input[contains(@id,'first') and contains(@id,'name')]")



sleep(5)
