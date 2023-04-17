def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    newlist = []
    for i in sudoku:
        newlist.append(i)
    newlist[row_no][column_no] = number
    sudoku = newlist
    return sudoku

def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s % 3 == 0 and s < 8:
                m += " "
            print(m, end="")

        print()
        r += 1
        if r % 3 == 0 and r < 8:
            print()

if __name__ == "__main__":

    sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("Original:")
    #print_sudoku(sudoku)
    print(id(print_sudoku(sudoku)))
    print()
    print("Copy:")
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    #print_sudoku(grid_copy)
    print(id(print_sudoku(grid_copy)))