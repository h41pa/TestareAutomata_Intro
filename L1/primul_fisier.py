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

# driver.find_element(By.ID,"job-title").send_keys("zugrav")
# sleep(2)


elemente_control = driver.find_elements(By.CLASS_NAME, 'form-control')
for ele in elemente_control:
    print(ele)
print(f'Avem {len(elemente_control)} elemente cu clasa form-control')
sleep(4)