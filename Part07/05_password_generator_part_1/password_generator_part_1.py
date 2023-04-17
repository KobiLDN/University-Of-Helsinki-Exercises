import string
from random import sample

def generate_password(length):
    letter_pool = string.ascii_lowercase
    generated_pass = sample(letter_pool, length)
    new_pass = ""
    for char in generated_pass:
        new_pass += char
    return new_pass

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))