def input_data():
    a = int(input("Value: "))
    return a

def count_value(a):
    if (a % 3) == 0:
        print("Yes")
    else:
        print("No")

count_value(input_data())

