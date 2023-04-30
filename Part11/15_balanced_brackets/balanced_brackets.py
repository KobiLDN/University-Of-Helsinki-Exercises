import string

def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    my_string = "".join([char for char in my_string if char in "()[]"])
    if not (my_string[0] == '(' and my_string[-1] == ')'):
        if not (my_string[0]) == "[" and my_string[-1] == "]":
            return False
        if (my_string[0]) == "[" and my_string[-1] == "]":
            return balanced_brackets(my_string[1:-1])
        return False


    # remove first and last character
    return balanced_brackets(my_string[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("x[[]")
    print(ok)