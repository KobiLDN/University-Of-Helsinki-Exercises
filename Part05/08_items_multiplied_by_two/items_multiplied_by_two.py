# Write your solution here
def double_items(numbers: list):
    newlist = [] #new blank list
    #numbers #original list
    for item in numbers:
        newlist.append(item * 2)
    return newlist

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)