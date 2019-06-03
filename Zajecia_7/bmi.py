def users_data():
    mass = float(input("Your weight: "))
    height = float(input("Your height: "))
    return mass, height

def counter(mass, height):
    bmi = round(mass / (height**2), 2)
    return bmi

def check(bmi):
    if bmi < 18.5:
        with open('niedowaga.txt') as niedo:
            return niedo.read()
    elif bmi > 25:
        with open('nadwaga.txt') as nad:
            return nad.read()
    else:
        with open('norma.txt') as norma:
            return norma.read()

def main():
    pass
