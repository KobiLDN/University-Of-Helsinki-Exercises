# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    newlist = []
    row = row_no
    eIndex = column_no
    count = 0
    for i in range(3):
        for i in range(3):
            newlist.append(sudoku[row][eIndex])
            eIndex += 1
        eIndex = column_no
        row += 1

    for i in newlist:
        if i > 0:
            if newlist.count(i) != 1:
                count += 1
    if count > 0:
        return False
    return True

if __name__ == "__main__":


    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]


    print(block_correct(sudoku, 1, 2))