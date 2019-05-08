# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość.
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy ( jest to prawdopodobne?)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.
print("-----------Does my fridge fits?-----------")
print("Please enter lenght, height and deepnes of your fridge and the elevator.")
print("The script will mesure if your fridge fits and how much space will be left.")

fridge_a = float(input("Height of fridge: "))
fridge_b = float(input("Lenght of fridge: "))
fridge_c = float(input("Deepnes of the fridge: "))

elevator_a = float(input("Height of the elevator: "))
elevator_b = float(input("Lenght of the elevator: "))
elevator_c = float(input("Deepnes of the elevator: "))

if fridge_a > elevator_a:
    print("Your fridge is to high! :O")
    exit()

if fridge_b > elevator_b:
    print("Your fridge is to long! :O")
    exit()

if fridge_c > elevator_c:
    print("Your fridge is to deep! :O")
    exit()

print("Nice your fridge fits into the elevator!")
print("A few informations in numbers:")
print("Elevators volume: ", elevator_a + elevator_b + elevator_c)
print("Fridge volume: ", fridge_a + fridge_b + fridge_c)

