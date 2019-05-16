def user_input():
    a = int(input("Do ilu silnie chcesz wygenerowac mistrzu?: "))
    return a

def count_silnia(a):
    i = 1
    b = a
    for i in range(1,b):
        a = a * i
    print(a)

count_silnia(user_input())

