# Write your solution here
def distinct_numbers(my_list):
    newlist = []    
    for i in my_list:
        if i in newlist:
            continue
        else:
            newlist.append(i)
    newlist.sort()
    return newlist

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]