def longest_series_of_neighbours(my_list):
    previous_i = 0
    current_i = 1
    current_count = 0
    longest_count = 0
    while current_i < len(my_list):
        # print(len(my_list))
        # print(my_list[current_i])
        # print(my_list[previous_i] + 1)
        # print(my_list[previous_i] - 1)
        if my_list[current_i] == my_list[previous_i]+1 or my_list[current_i] == my_list[previous_i]-1:
            current_count += 1
            if longest_count < current_count:
                longest_count = current_count
            current_i += 1
            previous_i += 1
        else:
            current_i += 1
            previous_i += 1
            current_count = 0
    return longest_count+1

if __name__ == "__main__":
    my_list = [1, 2]
    print(longest_series_of_neighbours(my_list))