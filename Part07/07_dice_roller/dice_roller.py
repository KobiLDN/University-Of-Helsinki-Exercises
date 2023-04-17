# Write your solution here
from random import choice, randint, random, sample

def roll(die: str):
    dieA = [3, 3, 3, 3, 3, 6]
    dieB = [2, 2, 2, 5, 5, 5]
    dieC = [1, 4, 4, 4, 4, 4]

    if die == "A":
        dieRandom = sample(dieA, 1)
    elif die == "B":
        dieRandom = sample(dieB, 1)
    else:
        dieRandom = sample(dieC, 1)
    for indian in dieRandom:
        return indian

def play(die1: str, die2: str, times: int):
    die1Score = 0
    die2Score = 0
    tie = 0
    for i in range(times):
        die1_number = roll(die1)
        #print(die1_number)
        die2_number = roll(die2)
        #print(die1_number)
        if die1_number > die2_number:
            die1Score += 1
        elif die2_number > die1_number:
            die2Score += 1
        else:
            tie += 1
    tally = (die1Score, die2Score, tie)
    return tally

if __name__ == "__main__":
    result = play("A", "C", 10)
    print(result)
    result = play("B", "B", 1000)
    print(result)
