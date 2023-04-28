# WRITE YOUR SOLUTION HERE:
# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]
# [<expression> for <item> in <series> if <Boolean expression>]
# <expression 1> if <condition> else <expression 2>
# [<expression 1> if <condition> else <expression 2> for <item> in <series>]

def lengths(string: list):
    return {word: len(word) for word in string}

if __name__ == "__main__":
    word_list = ["once", "upon" , "a", "time", "in"]

    word_lengths = lengths(word_list)
    print(word_lengths)