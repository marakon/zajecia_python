def get_items():
    items = []
    i = int(input("How many items to add: "))
    for item in range(0, i):
        item = input("Enter item: ")
        items.append(item)
    return items

def combine(items):
    print("Obierz all items.")
    for item in items:
        print("Add: " + item)
    print("Podsmaz")
    print("Enjoy")

combine(get_items())

