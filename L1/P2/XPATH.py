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


sleep(5)
