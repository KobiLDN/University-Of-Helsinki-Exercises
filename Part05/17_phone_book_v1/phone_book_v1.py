def phonebook(name, number):
    dict = {}
    dict["dave"] = "040-5466745"
    name = ""
    #dict[name] = number
    command = 0
    while command != "3":
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == "1":
            name = input("name: ")
            if name not in dict:
                print("no number")
                continue
            else:
                print(dict[name])
        elif command == "2":
            name = input("name: ")
            number = input("number: ")
            dict[name] = number
            print("ok!")
    print("quitting...")
phonebook("dave", "040-5466745")

