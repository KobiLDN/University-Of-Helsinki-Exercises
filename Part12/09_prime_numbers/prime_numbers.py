def prime_numbers():
    x = 1
    while True:
        if is_prime(x):
            yield x
        x += 1

def is_prime(x: int):
    if x < 2:
        return False
    for number in range(2, x):
        if x % number == 0:
            return False
    return True


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
