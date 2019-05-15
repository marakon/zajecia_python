def get_rating():
    r1 = int(input("First rating: "))
    r2 = int(input("Seconf rating: "))
    r3 = int(input("Third rating: "))
    return r1, r2, r3

def count_mean(r1, r2, r3):
    mean = (r1 + r2 + r3) / 3
    print("Mean value:", mean)
    return mean

def define_rating(mean):
    if mean > 7:
        print("Nice book")
    elif mean >= 4:
        print("so so")
    else:
        print("Shit")

(r1, r2, r3) = get_rating()
define_rating(count_mean(r1, r2, r3))

