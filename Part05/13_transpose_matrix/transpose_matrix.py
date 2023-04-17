def transpose(matrix: list):
    count = 0
    row = 0
    col = 0
    index = 0
    newlist2 = matrix[:]
    newlist = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            newlist.append(newlist2[row][col])
            count += 1
            row += 1
            if count == len(matrix):
                index += 1
                count = 0
                row = 0
                col += 1
        matrix[i] = newlist
        newlist = []

if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    transpose(matrix)

