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

sleep(5)
