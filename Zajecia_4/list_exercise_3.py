arr = []
ile = int(input("Ile liczb?: "))
for number in range(ile):
    number = int(input("Liczba: "))
    arr.append(number)

if arr[0] == arr[-1]:
    print(True)
else:
    print(False)

