from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# site_path_root = 'http://formy-project.herokuapp.com'
#
# # -- Selector NAME  ( nu este unic)
# driver_root = webdriver.Chrome()
# driver_root.get(site_path_root)
# lista_elemente = driver_root.find_elements(By.TAG_NAME, 'a')
# print(lista_elemente[17])
# elemnt_1 = lista_elemente[17]
# elemnt_1.click()
# sleep(3)
# driver_root.back()
# sleep(3)
# # ------------------------------------------------------------------
# # LINK TEXT
# link_autocomplete =driver_root.find_element(By.LINK_TEXT, 'Autocomplete')
# link_autocomplete.click()
# sleep(3)
# driver_root.back()
# sleep(3)
# #------------------------------------------------------------------
# # PARTIAL LINK TEXT
# link_auto_partial = driver_root.find_element(By.PARTIAL_LINK_TEXT, 'Switch') #Switch Window full text
# link_auto_partial.click()
# sleep(3)
# driver_root.back()
# sleep(3)