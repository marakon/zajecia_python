try:
    n = int(input("How many numbers?: "))
except ValueError:
    print('Enter int!')
    exit()
if n <= 0:
    raise Exception('You have to enter at least one element!')

sumer = 0
numbers = []
for number in range(n):
    value = int(input("Enter value: "))
    numbers.append(value)
    sumer += value

if sumer == 0:
    raise Exception('Moron')

for number in numbers:
    print(number)

print(sumer)

avg = sumer / n
print(avg)