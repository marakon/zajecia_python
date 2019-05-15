def get_password():
    password = input("Enter password: ")
    return password

def check_password(password):
    if len(password) < 8:
        print("Password to short!")
    elif password.islower() == True or password.isupper() == True:
        print("Co to za byki")
    elif password.isalpha() == True:
        print("Brakuje cyfry")
    elif password.isdecimal() == True:
        print("Ale gdzie litery?!")
    elif password.isalnum() == False:
        print("Gdzie te znaki?")
    else:
        print("Git majonez!")

check_password(get_password())

