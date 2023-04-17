def row_sums(my_matrix: list):
    sum = 0
    index = 0
    for i in my_matrix:
        for j in i:
            sum += j
        my_matrix[index].append(sum)
        sum = 0
        index += 1
if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)