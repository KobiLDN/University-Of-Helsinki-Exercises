class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __value(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()

    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()

    def __gt__(self, other: "SimpleDate"):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    pass
                elif self.day > other.day:
                    return True
                else:
                    return False
            if self.month > other.month:
                return True
            else:
                return False

        if self.year > other.year:
            if self.month > other.month:
                return True
            return True

        if self.year < other.year:
            return False

    def __lt__(self, other: "SimpleDate"):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    pass
                elif self.day < other.day:
                    return True
                else:
                    return False
            if self.month < other.month:
                return True
            else:
                return False

        if self.year < other.year:
            if self.month < other.month:
                return True
            return True

        if self.year > other.year:
            return False

    def __add__(self, number: int):
        new_day = self.day
        new_month = self.month
        new_year = self.year

        for days in range(number):
            if new_day == 30 and new_month < 12:
                new_day = 0
                new_month += 1
            elif new_day == 30 and new_month == 12:
                new_day = 0
                new_month = 1
                new_year += 1
            new_day += 1
        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, other: "SimpleDate"):
        selfies = self.day + (self.month * 30) + (self.year * 360)
        overies = other.day + (other.month *30) + (other.year * 360)
        x = selfies - overies
        return abs(x)