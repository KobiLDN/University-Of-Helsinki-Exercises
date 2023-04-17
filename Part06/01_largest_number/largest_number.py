# write your solution here

def largest():
    with open("numbers.txt") as new_file:             
        largest = 0        
        for number in new_file:
            if int(number) > largest:
                largest = int(number)
    return int(largest)

if __name__ == "__main__":
    print(largest())
    