def length_of_longest(my_list):
    newlist = []
    for i in my_list:
        newlist.append(len(i))
        newlist.sort()
    return newlist[len(newlist)-1]


if __name__ == "__main__":
    my_list = ["abc", "ab"]
    result = length_of_longest(my_list)
    print(result)