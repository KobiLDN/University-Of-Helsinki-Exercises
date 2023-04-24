# stringx = [str(number) for number in numbers]
# [<expression> for <item> in <series>]

class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    def __str__(self):
        return (f'Name:{self.name}, grade1: {self.grade1}' +
                f', grade2: {self.grade2}, grade3: {self.grade3}')

def best_results(results: list):
    return [max(result.grade1, result.grade2, result.grade3) for result in results]

    # list_of_STuf_f = []
    # for result in results:
    #     list_of_STuf_f.append(max(result.grade1, result.grade2, result.grade3))
    # return list_of_STuf_f
    
    # list_OF_bestGrade_s = []
    # for result in results:
    #     if result.grade1 > result.grade2 and result.grade1 > result.grade3:
    #         list_OF_bestGrade_s.append(result.grade1)
    #     elif result.grade2 > result.grade1 and result.grade2 > result.grade3:
    #         list_OF_bestGrade_s.append(result.grade2)
    #     else:
    #         list_OF_bestGrade_s.append(result.grade3)
    # return list_OF_bestGrade_s
if __name__ == "__main__":
    result1 = ExamResult("Peter", 5, 3, 4)
    result2 = ExamResult("Pippa", 3, 4, 1)
    result3 = ExamResult("Paul", 2, 1, 3)
    results = [result1, result2, result3]
    print(best_results(results))
