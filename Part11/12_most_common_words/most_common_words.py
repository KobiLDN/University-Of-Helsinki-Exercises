# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]
# [<expression> for <item> in <series> if <Boolean expression>]
# <expression 1> if <condition> else <expression 2>
# [<expression 1> if <condition> else <expression 2> for <item> in <series>]

import string


def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        fuf = file.read()
    #remove punctuations
    data = "".join([char for word in fuf for char in word if not char in "’'!?:,."]).split()

    # find words and add to dictionary with a count
    # new_dict = {}
    # for word in data:
    #     if not word in new_dict:
    #         new_dict[word] = 1
    #         continue
    #     new_dict[word] += 1
    #new_dict = {word: data.count(word) for word in data
    # 
    # if data.count(word) >= lower_limit}

    new_dict = {word: data.count(word) for word in data}

    #return words that appear more than or equal to lower limit
    # dict2 = {}
    # for key, values in new_dict.items():
    #     #print(key)
    #     #print(values)
    #     if values >= lower_limit:
    #         dict2[key] = values
    # return dict2

    return {word: count for word, count in new_dict.items() if count >= lower_limit}


if __name__ == "__main__":

    print(most_common_words("comprehensions.txt", 3))
