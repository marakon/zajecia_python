import bmi

def main():
    mass, height = bmi.users_data()
    print('So you weight {0} and your height is {1}'.format(mass, height))
    your_bmi = bmi.counter(mass, height)
    print(your_bmi)
    your_check = bmi.check(your_bmi)
    print('Your BMI is at {0} point, {1}'.format(your_bmi, your_check))

if __name__ == '__main__':
    main()
