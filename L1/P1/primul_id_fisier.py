"""
Elemente HTML:
HTML = Hyper Text Markup Language
Atunci cand vrem sa facem testare automata ne va interesa sa identificam elementele din codul de HTML,
deoarece sistemul automat nu va sti sa identifice elementele vizual, ci le va cauta dupa anumite cuvinte cheie.
Tag-urile sunt definite de semnele <> intre care se va pune numele tipului de element care este reprezentat. 
Tag-ul de final va avea aditional plasat caracterul /.
Exemplul de element de mai jos este un element de tip label care este reprezentat de doua perechi 
de elemente cheie:valoare (ca la dictionare) 
class = “no-control-label”
for = “loginform-email”
    <label class="no-control-label" for="loginform-email">Email</label>
Alte exemple de elemente web:
a (ancora), div (division), p (paragraph), input, span, ol (ordered list),
ul (unordered list), li(list item), table, th(table header), td(table data), tr (table row)
"""

"""
Un selector este un sir de caractere care are rolul de a identifica unul sau mai multe elemente
intr-o pagina web cu scopul de a interactiona cu ele in procesul de automatizare.
Exista mai multe tipuri de selectori, printre care:
ID
Class
Name
Link Text
Partial Link Text
XPATH
CSS Selector

Alegerea unui selector depinde de elementul pe care il cautam. 
Desi fiecare din ele vin la pachet cu propriile avantaje si dezavantaje,
noi vom folosi selectorii care ne ofera metoda cea mai usoara,
scurta si eficienta de a identifica un element in aplicatia web.

"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # numele 'driver' este cel mai intalnit
# va deschide automat o fila Chrome
sleep(2)

site_path = 'http://formy-project.herokuapp.com/form'
site_path_root = 'http://formy-project.herokuapp.com'
driver.get(site_path)
sleep(2)
# print(f'Title Page : {driver.title}')
# page_title = driver.title
# print(f'Title Page: {page_title}')

# driver.maximize_window() # mareste fereastra chrome
# sleep(2)
# driver.minimize_window() # micsoreaza fereastra chrome
# sleep(2)
print('#' * 50)
"""
driver.find_element - iti intoarce un singur match
driver.find_elements - iti intoarce o lista cu elemente ( exmple cnad cauti clasa si gasesti x) mai departe trebuie 
vazut care element ne trebuie noua, trebuie parcurs cu un for , un for each sa treci prin elementele respective.

"""
"""
Selectorii se cauta cu :
# - dupa id
. - clasa
"""

#     -SELECTORI-
# ----------------------------------------------------------------------------------
# -- Selector ID
# driver.find_element(By.ID, "first-name").send_keys("Modificare prin selector ID")
# driver.find_element(By.ID, "job-title").send_keys("Modificare prin selector ID")
# sleep(2)

#  -- Selector Class

# driver.find_element(By.CLASS_NAME, "form-control").send_keys("Aici s-a modificat cu selector clasa")
# # scrie peste cel la la first-name pentru ca a fost primul acela
# sleep(2)

# elements =  driver.find_elements(By.CLASS_NAME, "form-control")
# i = 0
# for element in elements:
#     print(f'{i}----|{element.text}|----')
#     if element.text:
#         pass
#     i += 1
#
# sleep(2)
# elem1 = elements[1]
# elem1.send_keys('Gata')
# sleep(2)

# i = 0
# for element in elements:
#     print(f'{i}----|{element.id}|----')
#     if element.id in 'EB7F4E1C3C39A794B799ECDCEF05CF4B_element_12':
#         element.send_keys('Modificat prin class')
#     i += 1
# sleep(5)

# elemente_control = driver.find_elements(By.CLASS_NAME, 'form-control')
# print(f'Avem {len(elemente_control)} elemente cu clasa form-control.')
# sleep(2)
