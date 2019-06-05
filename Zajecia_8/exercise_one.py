examples = [0.0, 10, 'one', ('cos', 5), {'klucz': 'wartosc'}]

for element in examples:
    print(element)
    print(type(element))

for element in examples:
    try:
        value = 10 // element
    except ZeroDivisionError:
        print("Nie dziel przez zero!")
    except TypeError:
        print("To zły typ zmiennej!")
    else:
        print("Wynik to:", value)
