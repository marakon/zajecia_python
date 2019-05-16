def get_numbers():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    return a, b, c

def sort_numbers(a, b, c):
    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    if c > a and c > b:
        print(c)

(a, b, c) = get_numbers()
sort_numbers(a, b, c)
