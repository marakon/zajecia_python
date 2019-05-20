lista = []
pierwsza = (1,3,5,7,9)
druga = (2,4,6,8,0)

lista = list(pierwsza[::2] + druga[1::2])
print(lista)

