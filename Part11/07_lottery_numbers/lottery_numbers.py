# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]
# [<expression> for <item> in <series> if <Boolean expression>]
# <expression 1> if <condition> else <expression 2>
# [<expression 1> if <condition> else <expression 2> for <item> in <series>]

class LotteryNumbers:
    def __init__(self, week: int, lottoNums: list):
        self.week = week
        self.lottoNums = lottoNums

    def number_of_hits(self, numbers: list):        
        return len([number for number in numbers if number in self.lottoNums])

    def hits_in_place(self, numbers: list):
        return [number if number in self.lottoNums else -1 for number in numbers]

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]
    print(week8.hits_in_place(my_numbers))
