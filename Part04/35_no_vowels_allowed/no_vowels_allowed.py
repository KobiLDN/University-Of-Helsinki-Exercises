# 1  which takes a string argument
# 2 The function returns a new string
# which should be the same as the original but with all vowels removed.
# You can assume the string will contain only
# characters from the lowercase English alphabet a...z.

# input inside the function
# variable = a e i o u
# for loop goes through the string

def no_vowels(my_string):
    vowels = "aeiou"
    word = ""
    for char in my_string:
        if char in vowels:
            continue
        word += char
        #print(word, end="")
    return word

if __name__ == "__main__":

    #my_string = "this is an example"
    print(no_vowels(my_string))