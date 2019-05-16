def get_data():
    string = input("Enter your string: ")
    return string

def check_string(string):
    if len(string) < 5:
        string.replace('a', 'z')
    print (string)

check_string(get_data())
