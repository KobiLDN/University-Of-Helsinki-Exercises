def read_input(askthem, lower, higher):
    while True:
        try:
            keep_arxing_them = input(askthem)
            numberz = int(keep_arxing_them)
            if numberz >= lower and numberz <= higher:
                return numberz
        except ValueError:
            pass
        print(f"You must type in an integer between {lower} and {higher}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 1, 20)
    print("You typed in:", number)