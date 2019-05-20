ile_osob = int(input("Ile masz osob: "))

lista = []

for osoba in range(ile_osob):
    name = input("imie: ")
    surname = input("nazwisko: ")
    poz = input("pozycja: ")
    lista.append([name, surname, poz])

for osoba in lista:
    print(' '.join(osoba))

