from selenium import webdriver
from selenium.webdriver.common.by import By
from  time import sleep

driver = webdriver.Chrome()

LINK = "https://the-internet.herokuapp.com/login"
driver.get(LINK)
driver.find_element(By.CSS_SELECTOR, "(//input)[1]")
sleep(4)