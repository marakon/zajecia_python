mass = int(input("Your weight: "))
height = float(input("Your height: "))

bmi = round(mass / (height**2), 2)
print("Your BMI: " + str(bmi))
