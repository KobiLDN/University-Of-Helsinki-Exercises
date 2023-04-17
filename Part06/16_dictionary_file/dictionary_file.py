while True:
    with open("dictionary.txt") as dict_file:
        dictionary1 = {"Finnish": [], "English": []}
        for word in dict_file:
            word = word.replace("\n", "")
            newfile = word.split(";")
            dictionary1["Finnish"].append(newfile[0])
            dictionary1["English"].append(newfile[1])
            #print(dictionary1)
    print("1 - Add word, 2 - Search, 3 - Quit")
    options = int(input("Function: "))
    if options == 1:
        finWord = str(input("The word in Finnish: "))
        dictionary1["Finnish"].append(finWord)
        engWord = str(input("The word in English: "))
        dictionary1["English"].append(engWord)
        newWord = f"{finWord};{engWord}"
        with open("dictionary.txt", "a") as add_to_dict_file:
            add_to_dict_file.write(newWord+"\n")
        print("Dictionary entry added")
    elif options == 2:
        search_term = str(input("Search term: "))
        count = 0
        for key, value in dictionary1.items():
            if search_term in value:
                for word in value:
                    count += 1
                    if search_term in word or search_term == word:
                        found = count
                        print(dictionary1["Finnish"][found-1], "-", dictionary1["English"][found-1])
    else:
        print("Bye!")
        break