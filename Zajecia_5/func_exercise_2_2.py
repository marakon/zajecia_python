def get_data():
    a = int(input("Numer1: "))
    b = int(input("Numer2: "))
    c = int(input("Numer3: "))
    return a, b, c

def minimum_of_two(x, y):
    return y if x > y else x

def max_of_two(x, y):
    return x if x > y else y

def max_of_three(x, y, z):
    return max_of_two(max_of_two(x,y),z)

def minimum_of_three(x, y, z):
    return minimum_of_two(minimum_of_two(x,y),z)

def main():
    (a, b, c) = get_data()
    max_num = max_of_three(a, b, c)
    min_num = minimum_of_three(a, b, c)
    print("Lowest: {0} \n Highest: {1}".format(min_num, max_num))

main()