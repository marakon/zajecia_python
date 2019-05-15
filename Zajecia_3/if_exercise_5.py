def get_password():
    password = input("Enter password: ")
    return password

def check_password(password):
    if len(password) < 8:
        print("Password to short!")
    elif password.islower() == True:
        print("Brakuje duzej litery")
    elif password.isalpha() == True:
        print("Brakuje cyfry")
    elif password.isdecimal() == True:
        print("Ale gdzie litery?!")
    else:
        print("Git majonez!")

check_password(get_password())

