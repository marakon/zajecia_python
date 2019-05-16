TEST_STRING = "abrakadabra"
def loop_slicing(string):
    new_string = ""
    for char in string:
        if char.index(char) % 2 != 0:
            continue
        new_string = new_string + char
    print(new_string)

loop_slicing(TEST_STRING)
