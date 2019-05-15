def users_data():
    mass = float(input("Your weight: "))
    height = float(input("Your height: "))
    return mass, height

def count_bmi(mass, height):
    bmi = round(mass / (height**2), 2)
    return bmi

def main():
    (mass, height) = users_data()
    print(count_bmi(mass, height))

main()