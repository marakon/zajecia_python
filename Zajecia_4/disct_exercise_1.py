list_to_dict = [
        ["klucz", "wartosc"],
        ["klucz2", "wartosc2"],
        ["klucz3", "wartosc3"]
        ]

dict_from_list = {}
for i in list_to_dict:
    dict_from_list[i[0]] = i[1]

print(dict_from_list)

