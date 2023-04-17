my_list = []
while True:
    word = input("please type in a word ")
    if word in my_list:
        break
    my_list.append(word)
print(f"You typed in", len(my_list), "different words")