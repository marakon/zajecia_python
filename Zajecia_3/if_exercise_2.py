def get_data():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    return a + b

def check_data(c):
    if c > 100:
        print(c)

check_data(get_data())
