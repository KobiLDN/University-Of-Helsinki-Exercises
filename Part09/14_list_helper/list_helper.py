class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        my_list.sort()
        mostCommonNumber = 0
        frequency = 0
        for number in my_list:
            x = my_list.count(number)
            if x > frequency:
                frequency = x
                mostCommonNumber = number
        return mostCommonNumber

    @classmethod
    def doubles(cls, my_list: list):
        count = 0
        unique_numbers = set(my_list)
        for number in unique_numbers:
            if my_list.count(number) >= 2:
                count+= 1
        return count

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))