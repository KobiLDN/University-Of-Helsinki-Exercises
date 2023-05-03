from random import choice

def word_generator(characters: str, length: int, amount: int):
    for j in range(amount):
        string = ""
        for i in range(length):
            string += choice(characters)
        yield string  

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
