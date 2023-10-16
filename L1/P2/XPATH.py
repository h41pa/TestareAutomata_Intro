"""
XPATH este un selector care ne permite navigarea intr-un cod HTML.

Putem sa folosim XPATH atunci cand niciuna din celelalte metode de identificare
nu ne-a ajutat sa gasim un element in interfata in mod unic.

Exista doua tipuri de XPATH:

XPATH absolut = identifica elementul pornind de la inceputul documentului pana in punctul in care elementul e identificat
XPATH relativ = identifica elementul pornind de la primul element unic gasit si navigand inainte sau
inapoi pana ajungem unde avem nevoie

Atunci cand vrem sa folosim XPATH-ul absolut putem pur si simplu sa dam click dreapta pe element,
click pe copy si apoi selectam Full Xpath.
Atunci cand vrem sa folosim XPATH-ul relativ putem pur si simplu sa dam click dreapta pe element,
click pe copy si apoi selectam Xpath

- NICIODATA nu este recomandat sa folosim XPATH-ul absolut pentru ca este unreliable.
Daca se schimba structura website-ului si se adauga vreun element inainte de elementul pe care il cautam noi,
adresa initiala nu va mai fi corecta si elementul nu va mai putea fi gasit.
- Desi este posibil sa copiem XPATH-ul relativ direct din browser,
 nu este o optiune recomandata pentru ca sansele sa va ofere cea mai scurta si buna varianta sunt mai mici.
 Cel mai bine este sa construim xpath-ul manual, care poate fi scris in mai multe forme

# --
Exemplu XPATH absolut: /html/body/div[1]/div/div/div[2]/div[4]/div/form/div[3]/button
Exemplu XPATH relativ pentru acelasi element: //button[@type="submit" and @name="login-button"]
Alt exemplu de XPATH relativ pentru acelasi element: //button[contains(text(),"Autentificare")]
Alt exemplu de XPATH relativ pentru acelasi element: //button[@type="submit" and @class="btn btn-cartu"]

- xpath ul absolut incepe cu caracterul “/” ca sa marcheze citirea de la inceputul documentului
- xpath-ul relativ incepe cu caracterele “//” ca sa marcheze citirea din interiorul documentului
de la o anumita pozitie

xpath: //button[@type="submit"]
 - caracterele “//” marcheaza inceputul cautarii pe baza de xpath relativ
 - cuvantul “button” marcheaza cautarea tuturor elementelor care au tag-ul button
 - caracterul “[” marcheaza inceputul cautarii de tip atribut=valoare
 - caracterul “@” anunta sistemul ca urmeaza sa fie dat un atribut de cautare
 - “type”  este atributul pe care il cautam
 - “submit” este valoarea atributului pe care il cautam
In traducere libera, xpath-ul de mai sus ar fi asa: cauta toate elementele de tip button care au tipul submit

putem avea si xpath: //*[@type="submit"]
 - caracterul “*” marcheaza cautarea tuturor elementelor indiferent de tag

XPATH-ul ne ofera avantajul major ca poate sa efectueze urmatoarele tipuri de cautari:

Din parinte in copil
Din copil in parinte
Din element in fratele ulterior
Din element in fratele anterior

Numim parinte orice element care are sub el mai multe alte elemente
Numim copil orice element care se afla in componenta unui alt element
Numim frate ulterior orice element care se afla dupa un alt element sub acelasi parinte
Numim frate anterior orice element care se afla inaintea unui alt element sub acelasi parinte

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

# Simbol not - se foloseste la negarea atributului
# Simbol not - negare logica
# o sa gaseasca in exemplul de mai jos , type tex sau orice alte type care nu sunt radio si checkbox
driver.find_element(By.XPATH, "//input[not(@type='radio') and not(@type='checkbox')]")

#
# AXIS NAVIGATION
#
"""
ancestor           - selecteaza toti stramosii elementului din care pornim - IN SUS
ancestor-or-self   - selecteaza toti stramosii elementului din care pornim + elementul din care pornim - IN SUS
parent             - selecteaza STRICT parintele elementului din care pornim - IN SUS
descendent         - selecteaza toti descendentii (copiii, copiii copiilor) elementului din care pornim - IN JOS
descendent-or-self - selecteaza toti descendentii + elementul din care pornim - IN JOS 
child              - selecteaza toti copiii nodului - IN JOS
following-sibling  - selecteaza fratii urmatorului element din care pornim - ACELASI NIVEL 
precending-sibling - selecteaza fratii precedenti ai elementului din care pornim - ACEKASI NIVEL
"""

# Stramosii <div> ai elementului label cu textul "First name"
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::div")

# TOTI stramosii elementului label cu textul "First name"
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::*")

# TOTI stramosii elementului label cu textul "First name" inclusiv <label>
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor-or-self::*")

# Parintele elementului <label> cu textul="First name" cu tag specificat
driver.find_element(By.XPATH, "//label[text()='First name']/parent::strong")
driver.find_element(By.XPATH, "//label[text()='First name']/parent::*")

# Toti descendentii elementului <div> avand clasa="input-group", indiferent de tip
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::*")  #toti
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::input") #doar input

# Toti descendentii elementului <div> avand clasa="input-group", indiferent de tip inclusiv cel din care pornim
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant-or-self::*")

# Toti copiii elementului <div> cu clasa="input-group" care sunt si ei de tip <div>
driver.find_element(By.XPATH, "//div[@class='input-group']/child::div")

# Toti fratii dupa elementul <option> cu atributul value=2 care sunt si ei de tot de tip option
driver.find_element(By.XPATH, "//option[@value=2]/following-sibling::option")
driver.find_element(By.XPATH, "//option[@value=2]/following-sibling::*")
# Toti fratii inaintea elementul <option> cu atributul value=3 care sunt si ei de tot de tip option
driver.find_element(By.XPATH, "//option[@value=3]/preceding-sibling::option")
driver.find_element(By.XPATH, "//option[@value=3]/preceding-sibling::*")
sleep(5)
