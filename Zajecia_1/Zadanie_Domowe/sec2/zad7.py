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
USD = 3.8
EUR = 4.3
cash = float(input("How much PLN do you have?: "))
cash_in_usd = round(cash/USD)
cash_in_eur = round(cash/EUR)
print("You have", cash_in_usd, "USD.")
print("You have", cash_in_eur, 'EUR.\n')

usd_200_bill = 0
usd_100_bill = 0
usd_50_bill = 0
usd_20_bill = 0
usd_10_bill = 0

eur_500_bill = 0
eur_200_bill = 0
eur_100_bill = 0
eur_50_bill = 0
eur_20_bill = 0
eur_10_bill = 0

while cash_in_usd > 200:
    usd_200_bill= usd_200_bill + 1
    cash_in_usd= cash_in_usd - 200
while cash_in_usd > 100:
    usd_100_bill= usd_100_bill + 1
    cash_in_usd= cash_in_usd - 100
while cash_in_usd > 50:
    usd_50_bill= usd_50_bill + 1
    cash_in_usd= cash_in_usd - 50
while cash_in_usd > 20:
    usd_20_bill = usd_20_bill + 1
    cash_in_usd = cash_in_usd - 20
while cash_in_usd > 10:
    usd_10_bill = usd_10_bill + 1
    cash_in_usd = cash_in_usd - 10

while cash_in_eur > 500:
    eur_500_bill = eur_500_bill + 1
    cash_in_eur = cash_in_eur - 500
while cash_in_eur > 200:
    eur_200_bill = eur_200_bill + 1
    cash_in_eur = cash_in_eur - 200
while cash_in_eur > 100:
    eur_100_bill = eur_100_bill + 1
    cash_in_eur = cash_in_eur - 100
while cash_in_eur > 50:
    eur_50_bill = eur_50_bill + 1
    cash_in_eur = cash_in_eur - 50
while cash_in_eur > 20:
    eur_20_bill = eur_20_bill + 1
    cash_in_eur = cash_in_eur - 20
while cash_in_eur > 10:
    eur_10_bill = eur_10_bill + 1
    cash_in_eur = cash_in_eur - 10

print("It means that you will have:")
print(usd_200_bill,'bills in 200.\n', usd_100_bill,'bills in 100.\n', usd_50_bill,'bills in 50.\n', usd_20_bill,'bills in 20.\n', usd_10_bill, 'bills in 10.\n', 'And the rest:', cash_in_usd,'USD.\n')
print(eur_500_bill,'bills in 500.\n', eur_200_bill,'bills in 200.\n', eur_100_bill,'bills in 100.\n', eur_50_bill,'bills in 50.\n', eur_20_bill,'bills in 20.\n', eur_10_bill, 'bills in 10.\n', 'And the rest:', cash_in_eur,'EUR.\n')

