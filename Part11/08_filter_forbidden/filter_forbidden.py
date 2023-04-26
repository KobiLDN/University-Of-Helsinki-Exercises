# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]
# [<expression> for <item> in <series> if <Boolean expression>]
# <expression 1> if <condition> else <expression 2>
# [<expression 1> if <condition> else <expression 2> for <item> in <series>]

def filter_forbidden(string: str, forbidden:str):
    # new_string = []
    # for char in string:
    #     if not char in forbidden:
    #         new_string.append(char)
    # new_string = "".join(new_string)

    new_string = "".join([char for char in string if char not in forbidden])
    return new_string

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)


