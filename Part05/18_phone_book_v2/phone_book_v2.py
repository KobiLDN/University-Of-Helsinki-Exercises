def phonebook():
    dict = {}
    name = ""
    command = 0
    while command != "3":
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == "1":
            name = input("name: ")
            if name not in dict:
                print("no number")
                continue
            else:
                for i in dict[name]:
                    print(i)
        elif command == "2":
            name = input("name: ")
            number = input("number: ")
            if name in dict:
                dict[name].append(number)
                print("ok!")
                continue
            dict[name] = [number]
            print("ok!")
    print("quitting...")
phonebook()