# write your solution here
def numbers1():
    new_List = []
    with open("matrix.txt") as new_file:
        for number in new_file:
            number = number.replace("\n", "")
            parts = number.split(",")
            for i in parts:
                new_List.append(int(i))
    return new_List

def matrix_sum():
    return(sum(numbers1()))
    #print(sum(numbers1()))

def matrix_max():
    return max(numbers1())
    #print(max(numbers1()))
    

def row_sums():
    temp1 = numbers1()
    count = 0
    row_lISt = []
    sum_of_list_thatWEare_going_toADD = 0
    for number in temp1:
        sum_of_list_thatWEare_going_toADD += number
        count += 1
        if count == 15:
            row_lISt.append(sum_of_list_thatWEare_going_toADD)
            count = 0
            sum_of_list_thatWEare_going_toADD = 0
    return row_lISt

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())