def input_data():
    names_string = input("Enter names seperated with spaces: ")
    return names_string

def view_welcome(names_string):
    names = names_string.split(" ")
    for name in names:
        print("Hi "+ name)

view_welcome(input_data())

