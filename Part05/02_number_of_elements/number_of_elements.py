def count_matching_elements(my_matrix: list, element: int):
    sum = 0
    for list in my_matrix:
        for i in list:
            if i == element:
                sum += 1
    return sum

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3], [1, 0, 0, 4]]
    print(count_matching_elements(m, 1))