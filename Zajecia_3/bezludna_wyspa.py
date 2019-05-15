def get_data():
    i = int(input("Ile bierzesz?: "))
    j = 0
    rzeczy = []
    while(j < i):
        rzeczy.append(input("Rzecz: "))
        j += 1
    return rzeczy

def pokaz(rzeczy):
    for n in rzeczy:
        print(n)
    print("To wszystko")

pokaz(get_data())
