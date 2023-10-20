"""
### TDD
TDD este prescurtarea de la Test Driven Development si este un proces de dezvoltare software
care se bazeaza pe transformarea cerintelor de business in teste inainte de a avea codul sursa dezvoltat.

TDD este in general implementat de catre echipa de dezvoltare prin definirea
a ceea ce se numesc teste unitare care vor testa ceea ce stim ca ar trebui sa faca sistemul.

Acele teste unitare vor fi rulate, si in mod firesc ele vor avea statusul de fail
pentru ca nu exista produsul software pe care ele il testeaza.

Ulterior se vor crea liniile de cod necesare pentru a implementa functionalitatea testata de acele
teste unitare dupa care ele se vor rerula. In momentul acesta asteptarea este ca ele sa aiba statusul passed.

In cazul in care acest lucru nu se intampla, codul va fi modificat si procesul va fi reluat
pana cand toate testele unitare vor fi passed.

Avantajele utilizarii unui TDD:

Ajuta la crearea minimului de cod optim necesar implementarii unei functionalitati
Se concentreaza pe teste, asigurand astfel o aplicatie mai apropiata de nevoile clientului
Asigura o acoperire mai mare a aplicatiei prin teste
Codul este mai usor de intretinut

"""

"""
### Testarea Unitara in contextul nivelurilor de testare

In procesul de software testing exista cinci niveluri de testare care reflecta testarea facuta 
la diverse grade de finalizare a aplicatiei: Unit testing, Integration testing, System testing si Acceptance testing

## Testarea unitară (sau de componente) e o modalitate prin care fiecare bucată individuală de cod 
este testată pentru a verifica dacă este pregatită pentru utilizare. Un test unitar reprezintă testarea celei mai mici bucăți funcționale dintr-o aplicație cum ar fi funcții, clase, proceduri, interefețe. 

## Testarea de integrare se concentrează pe interacțiunile dintre componente și sisteme si 
pe felul in care acestea comunica intre ele. Exista doua tipuri de testare de integrare:
- Integrare intre componente (cand doua sau mai multe module/componente sunt legate intre ele)
- Integrare intre sisteme (cand doua sau mai multe sisteme sunt legate intre ele)

## Testarea de sistem  - Se concentrează pe comportamentul și capabilitatea sistemului ca un tot unitar,
ținând cont de comportamentul end-to-end al funcționalităților pe care sistemul trebuie sa le execute,
ținând cont și de comportamentul non-funcțional așteptat al acelor taskuri. 

## Testare de acceptanță - Se concentrează pe comportamentul și capabilitățile sistemului ca un tot unitar.
Exista doua tipuri de testare de acceptanta: 

  ^ Alpha Testing - Ultima sesiune de testare înainte ca produsul să fie lansat publicului larg. 
Reprezintă testarea unei aplicații atunci când dezvoltarea este completă sau aproape completă. 
În urma testării alpha se pot face câteva schimbări minore dacă e necesar. 
Testarea are loc la site-ul dezvoltatorului și se realizează în două faze: 
    - Faza întâi în care software-ul este testat de către dezvoltatori;
    - Faza doi în care se face testarea de către echipa de QA într-un mediu similar cu cel al clientului.

  ^ Beta Testing - Are loc la site-ul clientului. Se va trimite sistemul/ softul la utilizatori, 
aceștia vor instala aplicația și vor începe sa o folosească în condiții reale. 
Scopul testării beta este să pună aplicația în mâinile unor utilizatori reali, 
oameni ce nu fac parte din echipa de dezvoltatori, pentru a descoperi defecte din perspectiva utilizatorului.

"""
"""
BDD este un proces de dezvoltare software derivata din TDD care se bazeaza pe o atentie mai mare 
asupra scenariilor de testare. 

Desi activitatile din suita BDD sunt similare cu cele din suita TDD, ele au un avantaj prin faptul 
ca adauga peste codul de testare automata fisierele descriptive ale scenariilor de business care 
sunt scrise intr-un limbaj pe care sa il inteleaga si utilizatorii care nu au cunostinte tehnice. 
Acestea se numesc feature files si sunt primele fisiere care se creeaza in procesul de BDD, 
iar tot ce va fi creat ulterior va fi pentru a valida testele descrise in acest feature file.

Fisierele de tip feature vor fi scrise intr-un limbaj numit GHERKIN care in python 
se afla implementat prin intermediul librariei behave (cucumber in java).

"""
"""
Gherkin este un limbaj descriptiv folosit in procesul de BDD pentru a putea implementa scenariile de business 
intr-un limbaj natural, scris intr-o engleza simpla astfel incat sa poata sa fie inteles de catre toate 
persoanele implicate. 

Exista mai multe elemente care pot fi folosite in limbajul gherkin, dar cele mai utilizate sunt: 
 GIVEN, WHEN, THEN, SCENARIO, SCENARIO OUTLINE, BACKGROUND

- Scenario - reprezinta testul pe care il facem. Spre exemplu: Verifica faptul ca utilizatorul
 se poate loga in aplicatie cu credentiale valide
- Scenario outline este folosit atunci cand vrem sa executam aceiasi pasi de mai multe ori cu diverse
 seturi de inputuri
- Given - descrie contextul in care se desfasoara actiunea, ca un fel de preconditii
- When - descrie pas cu pas ce ar trebui sa facem ca sa putem sa validam corectitudinea 
functionalitatii care ne intereseaza
- Then - descrie ce ar trebui sa se intample in urma secventei de activitati descrise prin When
- Background se foloseste atunci cand vrem sa dam un context general tuturor scenariilor din fisierul curent, 
astfel incat putem sa scriem un given o singura data si sa se propage la toate scenariile, 
in loc sa scriem cod redundant pentru fiecare scenariu

"""
"""
Daca pana acum am vorbit despre BDD, este important sa stiti ca BDD-ul 
se bazeaza pe ceea ce se numeste Page Object Model care este un design pattern.

Un design pattern reprezinta, asa cum ii spune si numele, un tipar de definire a codului. 
Sunt soluții la problemele generale cu care s-au confruntat dezvoltatorii de software în 
timpul dezvoltării software si care ne ajuta sa avem un cod mai stabil si mai bine structurat. 

Pentru BDD se foloseste in general un design care se numeste Page Object Model (POM) si 
care a fost implementat pentru gruparea tuturor elementelor dintr-o pagina web intr-un singur fisier python. 

Astfel, fiecare pagina web va avea ca si corespondent un singur fisier de python care va contine 
toate elementele dintr-o pagina web si respectiv toate actiunile care se pot face pe acea pagina web. 

"""
