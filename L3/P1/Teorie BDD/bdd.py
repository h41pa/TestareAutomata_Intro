"""
BDD - Behavior Driven Development
    - permite developerilor sa se focuseze pe testarea codului in functie de comportamentul aplicatiei
    - pentru faptul ca testele sunt scrise bazate pe comportament, sunt mai usor de inteles
    - bazat pe o strcutura de genul Given \ When \ Then
    Exemplu:
    Given un pas initial, o stare cunoscuta
    When genereaza un eveniment, o actiune careia ii testam output-ul
    Then verifica output, comportamentul este cel asteptat.
"""
"""
 - instalare pentru bdd : 
   - pip install behave
    - pip install behave-html-formatter

de asemenea trebuie plugins din 'download_these.png'instalate Cucumber, Gherkin, Ini
versiune de pycharm free in bdd nu o sa apara sugestii.
"""

#       # # # BDD -  structure
"""
~ Folders      
       features/ - aici sunt fisierele .feature , aici sunt fisierele in limbaj natural - given, when, then 
       pages/    - aici o sa contina clasele pentru fiecare pagina
       steps/    - contine maparea pasilor din "features" limbaj natural in logica din "pages" - 
                 corelarea dintre limbajul natural si functiile pe care noi le scriem efectiv in cod.
           

~ Inside folders: 

-   pages/base_page.py - foarte import pentru a creea toate metodele ajutatoare.
  - elementele comune care sunt in aceea pagina.( gen butoare care raman fixe le punem in base page, 
   toate paginile ulterioare vor avea elem care se gasesc in base page.
    Cream o CLasa BaseBage, aici cream metode ajutoare , pe care le putem folosi in  celelalte pagini sunt mai short.
     gen : find(locator , ca sa nu mai folosim self.driver.find_element(*locator) de fiecare data putem folosi direct:
       -self.find(locator) , ceea despacheteaza si putem folosi in base bage in urtoarele ,etode mai short
        gen click(self.find(locator).click()) , type , is_element_displayed , get_text , etc 
          exemplu : type definit in base_page

             def type(self, locator, text): 
                 self.find(locator).send_keys(text)

                 il putem folosi pe alte pagini direct folosind sintaxa:
                            self.type(locator, text)

~ Outside folders  on main BDD :

- driver.py configuratia driver sa porneasca
- environment.py - este un fisier prin care putem defini actiuni care sa fie facute inainte de
      fiecare test respectiv dupa fiecare test.
      Tot aici sunt instantate si obiectele din clasa care mapeaza pagina web ,
       fiecare pagina trebuie trecuta aici.

- behave.ini - pentru a face un raport, trebuie sa contina codul:
[behave.formatters]
html = behave_html_formatter:HTMLFormatter
 Prin acest ii spunem sa ne faca un raport html la testele noastre , pentru a rula  raportul folosim comanda:
 behave -f html -o numeleraportului.html 
  dupa ce genereaza pagina html ii dai click dreapta, open with -> browsers -> chrome

~~~~~

 ####  Ordinea de urmat :
 - fac folderele , features,pages,steps
 - driver.py , 
 - un fisier.feature in feature prin care descriu pasii de testare pentru fiecare feature, given,when,then
 - pages/base_page.py pentru a creea metodele ajutatoare.
 - tot in pages pagina pe care o testez cu toatele metodele si import BasePage,
     pentru a folosi metodele ajutoare,
 - environment.py pentru a defini conxtul in care rulam textul
 - steps/ si facem fisier pentru fiecare pagina din feature/ @given@when@then , def step_impl(context)
     pentru a lega intre ele :
      context.login_page.set_email - context.pagina.metoda pentru fiecare 
      actiune din fisierul .feature 
   
- pentru rulare folosim comanda "behave" in consola , fiind in folderul principal
- behave -f html -o numeleraportului.html ,  folosim comanda pentru a rula un raport html pentru test gen
                                                 behave -f html -o raport-initial.html
                            dupa ce genereaza pagina html ii dai click dreapta, open with -> browsers -> chrome


"""
