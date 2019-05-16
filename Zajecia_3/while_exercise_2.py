def game():
    secret = 5
    a = int(input("Give your number: "))
    while(a != secret):
        if a != secret:
            a = print("Wrong number! Try once again: ")
        else:
            break
    print("You won!")

game()
