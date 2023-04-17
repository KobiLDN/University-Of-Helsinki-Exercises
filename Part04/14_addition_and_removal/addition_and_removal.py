# Write your solution here
my_list = []
#listblank = []
number = 0
while True:
    print(f"The list is now {my_list}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "x":
        break
    if option == "d":
        number += 1
        if not my_list and number != 1:
            print("First number must be 1")
            continue
        if not my_list:
            my_list.append(number)
            continue
        if number <= my_list[-1]:
            print("value must be greater than the last item which is", my_list[-1])
        else:
            my_list.append(number)
    if option == "r":
        if not my_list:
            print("list is empty enter a value")
            continue
        my_list.pop(-1)
        if not my_list:
            number = 0
            continue
        else:
            number = my_list[-1]




print("Bye!")