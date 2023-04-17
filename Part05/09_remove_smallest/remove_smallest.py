# Write your solution here
def remove_smallest(numbers):
    newlist = numbers.copy()
    #print(min(newlist))
    newlist.remove(min(newlist))
    #print(newlist)
    numbers[:] = newlist

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)