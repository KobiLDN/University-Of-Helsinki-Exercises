def main():
    while True:
        word = input("enter word ")
        if palindromes(word) == True:
            return word
        print("that wasn't a palindrome")

def palindromes(string):
    return string == string[::-1]

printed = main()
print(printed, "is a palindrome!")