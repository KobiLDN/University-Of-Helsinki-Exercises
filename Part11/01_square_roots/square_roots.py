# WRITE YOUR SOLUTION HERE:
from math import sqrt

# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]

def square_roots(numbers: list):
    return [sqrt(number) for number in numbers]

if __name__ == "__main__":
    lines = square_roots([1,2,3,4])
    for line in lines:
        print(line)