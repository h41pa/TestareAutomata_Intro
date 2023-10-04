from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # numele 'driver' este cel mai intalnit
# sleep(2) # se deschide automat o fila Chrome

site_path = 'http://formy-project.herokuapp.com/form'
site_path_root = 'http://formy-project.herokuapp.com'
driver.get(site_path)
sleep(2)
# print(f'Title page: {driver.title} ') #Title page: Formy
page_title = driver.title
print(f'Page Title {page_title}')

driver.find_element(By.CSS_SELECTOR ,"select-menu")
sleep(2)


