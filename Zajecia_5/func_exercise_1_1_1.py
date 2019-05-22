def users_data():
    mass = float(input("Your weight: "))
    height = float(input("Your height: "))
    return mass, height

def count_bmi(mass, height):
    bmi = round(mass / (height**2), 2)
    return bmi

def check_bmi(bmi):
    if bmi < 18.5:
        print("Niedowaga")
    elif bmi > 25:
        print("Nadwaga")
    else:
        print("Norma")

def main():
    (mass, height) = users_data()
    bmi = count_bmi(mass, height)
    print(check_bmi(bmi))


main()