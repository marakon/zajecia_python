# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print("------------Currency calculator----------")
print("Please enter your budget in PLN.")
print("The script will convert your PLN budget and show you")
print('how much USD and EUR do you have for the vacations.\n')
cash = float(input("How much PLN do you have?: "))
print("You have", round(cash/3.8), "USD.")
print("You have", round(cash/4.3), "EUR.")

