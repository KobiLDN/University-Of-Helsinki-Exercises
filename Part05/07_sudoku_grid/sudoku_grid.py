def sudoku_grid_correct(sudoku: list):
    count = 0
    if row_correct(sudoku) == True:
        count += 1
    if column_correct(sudoku) == True:
        count += 1
    if block_correct(sudoku) == True:
        count += 1

    if count == 3:
        return True
    return False


def row_correct(sudoku):
    row = 0
    index = 0
    count = 0
    for i in range(len(sudoku)):
        for x in sudoku:
            for y in x:
                if y > 0:
                    if x.count(y) != 1:
                        count += 1
    if count > 0:
        return False
    return True

def column_correct(sudoku):
    count = 0
    newlist = []
    col = 0
    for i in range(len(sudoku)):
        for x in sudoku:
            newlist.append(x[col])
        for i in newlist:
            if i > 0:
                if newlist.count(i) != 1:
                    count += 1
        col += 1
        newlist = []
    if count > 0:
        return False
    return True

def block_correct(sudoku):
    newlist = []
    count = 0
    blocklist = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for rowcol in blocklist:
        row = rowcol[0]
        col = rowcol[1]
        for i in range(3):
            for i in range(3):
                newlist.append(sudoku[row][col])
                col += 1
            row += 1
            col = rowcol[1]
        for i in newlist:
            if i > 0:
                if newlist.count(i) != 1:
                    count += 1
        newlist = []

    if count > 0:
        return False
    return True

if __name__ == "__main__":
    sudoku = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 6, 0, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1],
    ]
    print(sudoku_grid_correct(sudoku))