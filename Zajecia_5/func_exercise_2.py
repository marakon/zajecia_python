def odd_or_not(lista):
    not_odd = []
    print(lista)
    for number in lista:
        if number % 2 == 0:
            print("Not")
            not_odd.append(number)
        else:
            print("Odd")
    return not_odd
