import string
from random import sample

def generate_strong_password(length: int, digits: bool, special: bool):
    new_pass = ""
    if digits and special:
        while len(new_pass) < length:
            letter_pool = string.ascii_lowercase
            generated_pool = sample(letter_pool, 1)
            new_pass += generated_pool[0]
            if len(new_pass) == length:
                break
            punc = "!?=+-()#"
            generated_punc = sample(punc, 1)
            new_pass += generated_punc[0]
            if len(new_pass) == length:
                break
            digits = string.digits
            generated_digit = sample(digits, 1)
            new_pass += generated_digit[0]
        return new_pass
    if not digits and not special:
        while len(new_pass) < length:
            letter_pool = string.ascii_lowercase
            generated_pool = sample(letter_pool, 1)
            new_pass += generated_pool[0]
        return new_pass
    if digits and not special:
        while len(new_pass) < length:
            letter_pool = string.ascii_lowercase
            generated_pool = sample(letter_pool, 1)
            new_pass += generated_pool[0]
            if len(new_pass) == length:
                break
            digits = string.digits
            generated_digit = sample(digits, 1)
            new_pass += generated_digit[0]
        return new_pass
    if not digits and special:
        while len(new_pass) < length:
            letter_pool = string.ascii_lowercase
            generated_pool = sample(letter_pool, 1)
            new_pass += generated_pool[0]
            if len(new_pass) == length:
                break
            punc = "!?=+-()#"
            generated_punc = sample(punc, 1)
            new_pass += generated_punc[0]
        return new_pass

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(6, True, True))