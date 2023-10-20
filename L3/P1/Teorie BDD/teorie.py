"""
Metode de Testare:

Black Box:
    Este o metoda de testare care este folosita fara sa stim structura interna a codului.
    Exemplu simplu: pentru un input avem un output la care ne asteptam. Daca primim outputul respectiv atunci putem
    spune ca aplicatia functioneaza corect fara sa ne punem problema structurii interne.
    Orientare - Funcționalitate
    Tipuri Erori gasite - Interfață utilizator, validare, utilizare date

White Box:
    Se bazeaza pe cunoasterea logicii interne a codului aplicatiei. Exemplu simplu: pentru un input avem un output
    asteptat. Daca primim outputul pe care il asteptam PLUS modul in care ajungem la rezultat, este cel asteptat,
    putem spune ca aplicatia functioneaza corect.
    Orientare - Logica
    Tipuri Erori gasite - Logică, performanță

Grey Box:
    Cum ii spune si numele este o combinatie intre Black Box si White Box. Practic Gray Box se bazeaza pe cunoasterea
    partiala a structurii interne / codului.
    Orientare - combinatie
    Tipuri Erori gasite - Logică, performanță, interfață utilizator

Tehnici de Black Box:
    Equivalence Partition: Exemplu, avem un input care accepta valori intre 1 si 15. Pentru testare alegem un numar care
    sa apartina fiecarui interval, adica un numar din intervalul <1, alt numar din intervalul 1-15 si alt numar > 15.
    Practic, prin validarea pe care o facem printr-un singur numar, presupunem ca tot intervalul din care face parte
    o sa se comporte la fel.

    Boundary Value Analysis: Exemplu, avem un input care accepta valori intre 1 si 15. Pentru testare alegem 2 numere
    care sa faca parte fix pe limitele intervalului. Incercam 0,1 cat si 15,16.

    Decision Table Testing: Exemplu, conditii logice. Avem 2 conditii logice care pot sa fie atat adevarate cat si false
        - Cazul in care conditia 1 este True, conditia 2 este False atunci actiunea 1.
        - Cazul in care conditia 1 este True, conditia 2 este True atunci actiunea 2.
        - Cazul in care conditia 1 este False, conditia 2 este True atunci actiunea 3.
        - Cazul in care conditia 1 este False, conditia 2 este False atunci actiunea 4.

    State Transition Testing: Exemplu, schimbari de stare. Bazata pe faptul ca testerul poate sa vada starile prin care
    trece softwareul, tranzitia in sine, cat si ce declanseaza schimbarea starii.
    Exemplu: Solida < - > Lichida < - > Vapori
        - Starea de start: Solida
        - Starea de final: Lichida
        - Starea de tranzitie: notata A

    Use Case Testing: Descrie interactiunea dintre un utilizator si system. De ajutor in momentul in care trebuie sa
    facem test case-uri pentru Integration Testing, System Testing si Acceptance Testing. Descrie practic procesul
    prin care trece un utilizator in folosirea system.
    Exemplu: Sistem de ATM
    Scenariu Principal de Happy Path:
        Pas 1: Utilizator: Introduce Card
        Pas 2: System: Valideaza card si intreaba de PIN
        Pas 3: Utilizator: Introduce PIN
        Pas 4: System: Valideaza PIN
        Pas 5: System: Permite accesul la Sold
    Extensii:
        Pas 2a: Cardul nu este valid
            System: Printeaza un mesaj si rejecteaza cardul
        Pas 4a: PIN nu este valid
            System: Printeze un mesaj si cere reintroducere PIN
        Pas 4b: PIN nu este valid de 3 ori
            System: Blocheaza cardul in ATM si iese din procesul de autentificare.

Tehnici de White Box:
    Statement Testing: Trece prin starile pe care le genereaza codul pe care il testez. Exemplu, introduc doua numere
    de la tastatura si sa mi le compare.
    if var_A > var_B:
        # Execute code if True
        print("var_A este mai mare")
    else:
        # Execute code if False
        print("var_B este mai mare")
    Trebuie sa verificam ca trece prin ambele stari, atat data var_A > var_B cat si invers.
    IMPORTANT: Focusul este pe stare

    Decision Testing: Trece prin decizile pe care trebuie sa le ia codul care trebuie sa il testez. Exemplu, introduc
    doua numbere de la tastatura si sa mi le compare.
    if var_A > var_B:
        # Execute code if True
        print("var_A este mai mare")
    else:
        # Execute code if False
        print("var_B este mai mare")
    Trebuie sa verificam ca trece prin ambele decizii, atat daca var_A > var_B cat si invers.
    IMPORTANT: Focusul este pe decizie

### Piramida de testare este compusa din 4 niveluri de testare: ###

~Unit Testing - Component Testing - White Box
    Se concentreaza pe testarea modulului respectiv - exemplu selectez o lista de laptopuri si afiseaza ce cer.

~Integration Testing - Black Box, Gray Box, White Box
    Modulele de cod sunt testate ca group pentru a scoate in evidenta interactiunea dintre ele si daca functioneaza
    conform specs

    - Component Integration Testing: Se testeaza integrarea componentelor
    - System Integration Testing: Se testeaza integrarea sistemelor

    Are mai multe abordari posibile:
    - BingBang: Toate modulele combinate impreuna si testate dintr-o data; focusul este pe interactiunea intre module
    - TopDown: Modulele de pe nivelul superior sunt testate prima data apoi nivelul inferior de module
    - BottomUp: Modulele de pe nivelul inferior sunt testate prima data apoi nivelul superior de module
    - Sandwich/Hybrid o combinatie intre TopDown si BottomUp

~System Testing - Black Box
    Este un nivel de testare unde un software complet integrat este testat. Scopul testului este de a evalua tot
    sistemul

~User Acceptance Testing: Black Box
    Se testeaza daca softwareul indeplineste cerintele clentului, cerintele de business.
    Exista doua tipuri de UAT
    - Alpa Testing: Se testeaza de membrii organizatiei
    - Beta Testing: Se testeaza pe end useri.

Ce este Agile ?
    Dat fiind faptul ca procesul de dezvoltare poate dura destul de mult ( de exemplu chiar si in cateva luni contextul
    de business se poate schimba ) au luat amploare diverse metodologii de lucru, Agile fiind una dintre ele si cea mai
    populara.
    Agile este o modalitate de a gestiona un proiect prin impartirea lui in mai multe faze, incrementale. Agile isi
    propune sa lucreze cate putin, frecvent si incremental ( un ciclu de dezvoltare poate sa dureze undeva la 3-4
    saptamani, ideal ) a.i. sa se poate adapta nevoilor de business mai rapid.

Agile Testing Methods:

TDD - Test Driven Development
     Proces:
    - Scriem un test care sa cuprinda practic cerinta de business
    - Ruleaza testul care ar trebui sa dea fail, pentru ca nu exista codul scris
    - Dezvoltatorul scrie codul si reruleaza testul pana cand este pass
    - Refactorizeaza codul daca este necesar dupa ce testul este deja pass
    - repeta testul pentru toate secventele de cod ulterioare

ATDD - Acceptance Test Driven Development
    - defineste criteriul final de acceptare al software-ului
    - rezolutie rapida a bug-urilor si impactul lor asupra output-ului final

BDD - Behavior Driven Development
    - permite developerilor sa se focuseze pe testarea codului in functie de comportamentul aplicatiei
    - pentru faptul ca testele sunt scrise bazate pe comportament, sunt mai usor de inteles
    - bazat pe o strcutura de genul Given \ When \ Then
    Exemplu:
    Given un pas initial, o stare cunoscuta
    When genereaza un eveniment, o actiune careia ii testam output-ul
    Then verifica output, comportamentul este cel asteptat.

Ce este un Design Pattern ?
    Sunt niste modele de proiectare si reprezinta niste solutii generale si reutilizabile ale unei probleme comune
    in design-ul unui software

POM ( Page Object Model ) este un Design Pattern.
    - un design pattern folosit in testarea automata
    - folozofia principala este sa reprezinte fiecare pagina web ca o clasa
    - In clasa respectiva o sa gasim toate elementele ce tin de pagina pe care o reprezinta
    - Poate sa fie folosit in mai multe limbaje sau framework-uri ca ex. Python + Pytest, Java + TestNG, samd.
    - Oricand este nevoie sa interactioneze cu interfata web, testele folosesc metode din clasa ce reprezinta pagina
    respectiva
"""

