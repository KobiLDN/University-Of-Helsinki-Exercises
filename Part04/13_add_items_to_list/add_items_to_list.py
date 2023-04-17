# Write your solution here
counter = 0
items = 0
numbers = []
items = int(input("how many items: "))
while counter < items:
    value = int(input("Enter value: "))
    counter += 1
    #print("Item", counter, ":", value)
    numbers.append(value)
print(numbers)



