# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    numbaz = set()
    while len(numbaz) < amount:
        lottoNumber = randint(lower, upper)
        numbaz.add(lottoNumber)
    list(numbaz)
    return sorted(numbaz)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)