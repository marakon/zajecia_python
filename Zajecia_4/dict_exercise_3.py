jaki_znak, ile = input("Znak?: "), int(input("Ile: "))
bajer = [[jaki_znak]* ile] * ile

print(list(' '.join(x) for x in bajer))
