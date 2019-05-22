import func_exercise_2 as f

def get_data():
    lista = []
    ile = int(input("Ile elementow: "))
    for num in range(ile):
        num = int(input("Liczba: "))
        lista.append(num)
    return lista

lista = get_data()
not_odd = f.odd_or_not(lista)
print(not_odd)
