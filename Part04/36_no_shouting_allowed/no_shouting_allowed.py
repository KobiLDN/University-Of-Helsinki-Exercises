# Write your solution here
def no_shouting(zorro):
    newlist = []
    #uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word in zorro:
        if word.isupper():
            continue
        else:
            newlist.append(word)
    return newlist

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)