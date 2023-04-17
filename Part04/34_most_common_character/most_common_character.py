def most_common_character(first_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newlistA = []
    newlistB = []

    for letter in alphabet:
        if first_string.count(letter) == 0:
            continue
        elif first_string.count(letter) > 0:
            newlistA.append(letter)
            newlistB.append(first_string.count(letter))
    print(newlistA)
    print(newlistB)
    #
    return newlistA[newlistB.index(max(newlistB))]

    #print(f"{letter} appears {first_string.count(letter)} times")







if __name__ == "__main__":
    first_string = "apppppbcdbdzzzzze"
    print(most_common_character(first_string))