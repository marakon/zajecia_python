def kawalek(i, szerokosc):
    for rozmiar in range(1, i+1, 2):
        print((rozmiar * "*").center(szerokosc))

def cala(rozmiar):
    for i in range(3, rozmiar+1, 2):
        kawalek(i, rozmiar)

i = int(input("Szerokosc?: "))
cala(i)
