lista = []

def get_numbers():
    ile = int(input("Ile liczb: "))
    for liczba in range(ile):
        liczba = int(input("Liczba: "))
        lista.append(liczba)
    return lista

def calc_lista(lista):
    licz = 0
    for liczba in lista:
        licz += liczba
    return licz

number = get_numbers()
calc = calc_lista(number)
print("Suma: {0}".format(calc))

