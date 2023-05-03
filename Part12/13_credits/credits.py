from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


# Write your solution
def sum_of_all_credits(course_deets: list):
    return reduce(lambda course_deets, item: course_deets + item.credits, course_deets, 0)


def sum_of_passed_credits(course_deets: list):
    x = filter(lambda course_attempts: course_attempts.grade >= 1, course_deets)
    return reduce(lambda something, item: something + item.credits, x, 0)

    #return reduce(lambda course_deets, item: course_deets + item.credits if item.grade >= 1 else course_deets, course_deets, 0)


def average(course_deets: list):
    x = list(filter(lambda course_attempts: course_attempts.grade >= 1, course_deets))
    return reduce(lambda something, item: something + item.grade, x, 0) / len(x)

    #return reduce(lambda course_deets, item: course_deets + item.grades if item.grade >=1 else course_deets, course_deets, 0) 

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)