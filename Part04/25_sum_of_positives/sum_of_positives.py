def sum_of_positives(my_list):
    sum_list = []
    for i in my_list:
        if i > 0:
            sum_list.append(i)
    return sum(sum_list)


if __name__ == "__main__":
    my_list = [1, -1, 2, -2, 3, -3]
    sum_of_positives(my_list)
    result = sum_of_positives(my_list)
    print("The result is", result)