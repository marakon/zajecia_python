arr = []
i = int(input("Ile przedmiotów?"))
for item in range(i):
    item = input("Co dodajesz?: ")
    arr.append(item)

sorted_list = arr.sort()

for item in sorted_list:
    print(item)
