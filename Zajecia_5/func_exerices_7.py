def get_number():
    number = input("Podaj numer karty")
    len_num = len(number)
    if len_num not in [13,15,16]:
        print("Spadaj gosciu!")
        exit()
    return number

def is_visa(number):
    len_num = len(number)
    if len_num not in [13,16]:
        return False
    else:
        if number[0] == '4':
            return True
        else:
            return False

def is_mc(number):
    len_num = len(number)
    if len_num != 16:
        return False
    else:
        if 51 <= int(number[:2]) <= 55:
            return True
        elif 2221 <= int(number[:4]) <= 2720:
            return True
        else:
            return False

def is_ae(number):
    len_num = len(number)
    if len_num != 15:
        return False
    else:
        if int(number[:2]) in [34, 37]:
            return True
        else:
            return False

def main():
    card_number = get_number()
    if is_ae(card_number): print("To americanexpoers")
    if is_mc(card_number): print("to mastercard")
    if is_visa(card_number): print("to visa")
    else: print("Nie znam")

main()