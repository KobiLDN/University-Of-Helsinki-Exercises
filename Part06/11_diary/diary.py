while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    options = int(input("Function: "))
    if options == 1:
        with open("diary.txt", "a") as my_file:
            diary_entry = str(input("Diary entry: "))
            my_file.write(diary_entry+"\n")
            print("Diary saved")
            continue
    elif options == 2:
        with open("diary.txt", "r") as my_file:
            print("Entries:")
            for i in my_file:
                print(i)
            continue
    elif options == 0:
        print("Bye now!")
        break