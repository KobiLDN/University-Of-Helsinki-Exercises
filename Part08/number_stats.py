class NumberStats:

    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number: int):
        self.numbers += number
        self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        if self.numbers == 0 or self.count == 0:
            return 0
        return self.numbers

    def average(self):
        x = self.numbers
        y = self.count
        if y == 0:
            return 0
        else:
            return x / y

stats = NumberStats()
even = NumberStats()
odd = NumberStats()
ask = 0
while (ask := int(input("Please type in integer numbers: "))) != -1:
    if ask == -1:
        break
    stats.add_number(ask)
    if ask % 2 == 0:
        even.add_number(ask)
    else:
        odd.add_number(ask)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())
