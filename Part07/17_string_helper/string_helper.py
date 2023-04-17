import string

def change_case(orig_string: str):
    newstring = ""
    for char in orig_string:
        if char == " ":
            newstring += " "
        if char.isupper():
            newstring += char.lower()
        elif char.islower():
            newstring += char.upper()
    return newstring

def split_in_half(orig_string: str):
    middleOfString = len(orig_string) // 2
    newstring = (orig_string[:middleOfString], orig_string[middleOfString:])
    return newstring

def remove_special_characters(orig_string: str):
    newstring = ""
    for char in orig_string:
        if char in string.ascii_letters or char in string.digits or char in string.whitespace:
            newstring += char
    return newstring

if __name__ == "__main__":
    my_string = "Well hello there!"
    change_case(my_string)
    split_in_half(my_string)
    remove_special_characters(my_string)
    print(remove_special_characters(my_string))

    # p1, p2 = string_helper.split_in_half(my_string)
    #
    # print(p1)
    # print(p2)
    #
    # m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    # print(m2)