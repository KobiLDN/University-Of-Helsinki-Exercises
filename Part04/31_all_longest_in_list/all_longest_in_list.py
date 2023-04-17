# Write your solution here
def all_the_longest(spiderman):
    newlist = []
    longest_name = ""
    for name in spiderman:
        if len(name) >= len(longest_name):
            #print(name)
            longest_name = name

    for name in spiderman:
        if len(name) == len(longest_name):
            newlist.append(name)

    return newlist

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']