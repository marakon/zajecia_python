""" Stwórz listę 10 elementową (różne typy!).
    Pozwól użytkownikowi podać dowolny index.
    Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy."""

our_list = [0, 2, ('three'), 'f', 5, {6: 6}, [1, 2, 3], {'8': '8'}, 'nine', 10]

print("This is our list:")
for element in our_list:
    print(element)
n = int(input("Choose one index from 0-9: "))

if isinstance(our_list[n], str):
    raise Exception("It's a string!")

if isinstance(our_list[n], tuple):
    raise Exception("It's a tuple!")

if isinstance(our_list[n], dict):
    raise Exception("It's a dict!")

if isinstance(our_list[n], list):
    raise Exception("It's a list!")

try:
    value = 1 / our_list[n]
except ZeroDivisionError:
    print("Do not divide by 0!")
else:
    print(value)

