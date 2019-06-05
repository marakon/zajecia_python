def users_data():
    mass = float(input("Your weight: "))
    height = float(input("Your height: "))
    return mass, height

def counter(mass, height):
    return round(mass / (height**2), 2)

def check(bmi):
    if bmi < 18.5:
        open_file('niedowaga.txt')
    elif bmi > 25:
        open_file('nadwaga.txt')
    else:
        open_file('norma.txt')

def open_file(file):
    with open(file) as f:
        return f.read()

def main():
    pass
