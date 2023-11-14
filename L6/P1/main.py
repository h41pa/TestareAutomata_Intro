# 1. Ce este o variabila in Python?
# Variabila - un container din memorie a carui valoare poate sa se schimbe
# de mai multe ori de-a lungul executiei programului

x = 10
name = 'Andrei'
sir = [1, 2, 3, 4]

# 2. Cum afisam un mesaj in consola?
print("Mesaj") # Output: Mesaj
print("Name: ", name) # Output: Name: Andrei

# 3. Care este diferenta dintre o functie si o metoda, dar dintre argumente si parametrii?

# Metoda - apartine unei clase si se defineste in interiorul acesteia
#        - are ca si parametru mereu acel self
#        - def metoda(self, params)

# Functia - def nume_functie(param1, param2, param3)

# Parametri si argumente?
# Parametri sunt acele variabile care se definesc
# in interiorul unei declaratii de functie sau metoda
# si pot sa ia mai multe valori trimise la apel

# Argumentele sunt acele valori pe care le trimitem la apelul functiei
# si care vor fi preluate de catre parametrii functiei apelate

# def date_personale(nume, varsta, salariu, params)
# date_personale('Andrei', '28', '9000', arguments)

# 4. Ce tipuri de date cunosti?

# string
ingredient = "masline"
# float
pret = 25.6
# integer
nota = 9
# boolean (True, False)
este_cald = True

# 5. Cum putem sa extragem un subsir de caractere dintr-un string?
nume = "Ana Popa"

lista_caractere = nume.split()
print(lista_caractere) # ['Ana', 'Popa']

print(nume[0:3]) # Ana
print(nume[:3]) # Ana
print(nume[-1]) # ultimul caracter
print(nume[-3:-1]) # op
print(nume[-3:]) # opa

# 6. Caracterizarea urmatoarele structuri de date din punct de vedere
# al mutabilitatii (mutabil/imutabil) si al ordonarii (ordonat/neordonat):

# - liste
my_list = [True, 'Ana', 2.5, 10]
# mutable/immutable: MUTABLE (se pot adauga, sterge, modifica valori)
# ordered/unordered: ORDONATE

# adaugarea unui nou element in lista
my_list.append('masline')

# concatenare liste
# v1
ny_list = my_list + ['Capsuni', 'Struguri', 2]
# v2
my_list.extend([1, 2, 3])
print(my_list)
print(ny_list)
print(ny_list[4])





# - dictionare
# mutable/immutable - Mutable
# ordered/unordered - Unordered
my_dict = {
    "Ioan": 30,
    "Ana": 16
}
# adaugarea unui element nou in dictionar
# v1
my_dict.update({"Alina": 23})
# v2
my_dict["Larisa"] = 10

print(my_dict)

# actualizarea unui element din dictionar
my_dict["Ana"] = 18

# stergerea
my_dict.pop("Larisa")
print(my_dict)

# accesarea elemente dictionar
print(my_dict['Ana'])

# - tupluri
# mutable/immutable: Immutable
# ordered/unordered: Ordered

coordonate = (12.34, 26)
my_tuple = (3,)
print(my_tuple[0])
print(coordonate[0])
print(coordonate[1])

# - seturi
# mutable/immutable: Mutable
# ordered/unordered: Unordered

my_set = {"capsuni", 1, "ceva"}
my_set.add('lamai')

my_set.pop()
print(my_set)

# 7. Ce este o exceptie in Python si cum poate fi tratata?

# Exceptie = eroare/situatie in care nu poate fi executat codul
# Ca sa aruncam o exceptie din cod -> raise <exception>
# Ca sa tratam o exceptie: try/except catch
# Cum ridicam o exceptie? => raise
def division_by_zero():
    a = 20
    b = 0

    if b != 0:
        print(a/b)
    else:
        raise ZeroDivisionError

# Cum putem trata o exceptie ? try/except
# Putem avea intr-un set elemente care sunt mutabile?
# Nu, elementele dintr-un set sunt IMUTABILE
# my_set.add([1,2])

def add_element(set, element):
    try:
        set.add(element)
    except TypeError:
        print("Nu putem adauga elemente mutabile intr-un set")

add_element(my_set, 12)
add_element(my_set, [1, 2])


# 8. Ce sunt functiile in Python?
# un bloc de cod care are o logica proprie
# avantajul unei functii este ca o definim o singura data
# iar mai apoi o putem apela de ori cate ori avem nevoie
# eliminand codul duplicat

# 9. Ce sunt clasele in Python?
# O clasa in Python este un sablon/template/blueprint din care se vor crea
# obiecte si in care o sa definim proprietatile/atributele si comportamentul/actiunile
# caracteristice obiectelor instantiate

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def latra(self):
        pass

    def manance(self):
        pass

    def musca(self):
        pass

# 9. Care sunt principiile OOP?
# 1. Mostenirea - abilitatea de a crea o noua clasa din o clasa deja existenta
# cu scopul de a reutiliza logica si proprietatile clasei parinte si a mosteni metodele ei
# 2. Polimorfism - avem metode definite in clasa parinte, vrem sa le redefinim logica in clasa
# copil pentru o metoda care are nume identic in ambele clase
# 3. Abstractizarea - abstractizam proprietati comune ale obiectelor in clase si le reprezentam prin atribute si metode
# 4. Incapsularea - este un mecanism prin intermediul caruia se leaga date si functii impreuna
# cu scopul de a manipula date si de a le tine sigur pentru accesul din exterior
# Cum se face?
# - gruparea datelor si functiilor
# - restrictionarea acesului (private, protected, public)
# public
# _protected
# __private

# Ce face blocul eslte atasat unui ciclu repetitiv

my_list1 = [1, 2, 4, 5]

for element in my_list1:
    if element == 3:
        print(element)
        break
    print(element)
else:
    # codul care se executa la finalul unei iteratii
    # atata timp cat iteratia a akuns la final
    # nu a fost intrerupta executia for-ului
    print("hello")


# Cum se poate inversa un string?
my_str = "abc"
print(reversed(my_str))
print(my_str)
print(my_str[::-1])

# Care este diferenta dintre o interfata si o clasa abstracta ?

# interfata -> contine doar metode abstracte (metode fara implementare concreta)
# clasa abstracta -> contine atat metode abstracte cat si metode cu implementare concreta (unele metode au deja cod implementat)


# Ce reprezinta parametrul self folosit in clasa?
# este un parametru obligatoriu pentru toate metodele dintr-o clasa
# si face referire la obiectele care urmeaza sa fie instantiate din clasa respectiva

# avand acest self ca si parametru in interiorul clasei,
# am acces la toate atributele clasei definite prin self si la metodele clasei


# Ce reprezinta parametrul super()?

# super -> superclass (clasa superioara/parinte)
# am acces la toate atributele si metodele clasei parinte prin apelul super().

















