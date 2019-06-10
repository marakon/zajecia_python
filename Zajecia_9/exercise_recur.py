def wypisz(n):
    if n < 0:
        print('-')
        n -= n
    if n // 10 is not 0:
        wypisz(n // 10)
    
    print(n % 10)


wypisz(1234)

#1 wypisz -> 123 -> 3
#2 wypisz -> 12 -> 2
#3 wypisz -> 1 -> 1