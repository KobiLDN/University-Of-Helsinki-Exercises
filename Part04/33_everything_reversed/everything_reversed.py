def everything_reversed(my_list):
    item = len(my_list) - 1
    new_list = []
    while item >= 0:
        reverse = my_list[item]
        reverse = reverse[::-1]
        new_list.append(reverse)
        #print(reverse)
        item -= 1
    return new_list


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)