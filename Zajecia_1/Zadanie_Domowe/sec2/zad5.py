# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1, " divided by ", num2, " equals ", num1 / num2)
print(num1, " fits ", round(num1 / num2,0), " times in ", num2)
print("Modulo from ", num1, " and ", num2, " equals ", num1 % num2)

