import string

def separate_characters(my_string: str):

    listOascii = ""
    listOpuncs = ""
    listOothers = ""

    for char in my_string:                              # asci onlyFans
        if char in string.ascii_letters:
            listOascii += char
        elif char in string.punctuation:
            listOpuncs += char
        else:
            listOothers += char

    ma_tuple = (listOascii, listOpuncs, listOothers)
    return ma_tuple

if __name__ == "__main__":

    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])