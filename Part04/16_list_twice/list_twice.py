my_list = []
number = -1
while True:
    number = int(input("New item: "))
    if number == 0:
        break
    else:
        my_list.append((number))
        print("The list now:", my_list)
        print("The list in order:", sorted(my_list))
print("Bye!")