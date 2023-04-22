class Course:
    def __init__(self, course: str, grade: int, credits: int):
        self.__course = course
        self.__grade = grade
        self.__credits = credits

    def course(self):
        return self.__course

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def add_course(self, course: str, grade: int, credits: int):
        self.__course = course
        self.__grade = grade
        self.__credits = credits


class courseRecords:
    def __init__(self):
        self.__course_data = {}

    def add_course(self, course: str, grade: int, credits: int):
        if not course in self.__course_data:
            self.__course_data[course] = {}
        if not grade in self.__course_data[course] or credits > self.__course_data[course][grade]:
            self.__course_data[course][grade] = credits

    def get_course_data(self, course: str):
        if not course in self.__course_data:
            return None
        return self.__course_data[course]

    def statistics(self):
        return self.__course_data

class courseRecordsApplication:
    def __init__(self):
        self.__courseRecords = courseRecords()

    def help(self):
        print("commands")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courseRecords.add_course(course, grade, credits)

    def get_course_data(self):
        course_name = input("course: ")
        course = self.__courseRecords.get_course_data(course_name)
        if course is None:
            print("no entry for this course")
        else:
            grade = 0
            for key, value in course.items():
                if key > grade:
                    grade = key
                    credits = value

            print(f"{course_name} ({credits} cr) grade {grade}")

    def statistics(self):
        course = self.__courseRecords.statistics()
        completed_courses = len(self.__courseRecords.statistics())
        grade = 0
        gradeTimesCredits = 0
        total_grade_value = 0
        totalCredits = 0
        grade_distribution = {}

        for key, value in course.items():
            for key, value in value.items():
                if int(key) > int(grade):
                    grade = int(key)
                    credit = int(value)
            gradeTimesCredits += (grade * credit)
            totalCredits += credit
            total_grade_value += grade
            if not grade in grade_distribution:
                grade_distribution[grade] = 1
            else:
                grade_distribution[grade] += 1
            grade = 0
        mean = total_grade_value / completed_courses

        print(f"{completed_courses} completed courses, a total of {totalCredits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for grade in [5, 4, 3, 2, 1]:
            print(f"{grade}: {'x' * grade_distribution.get(grade, 0)}")

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.add_course()
            if command == "2":
                self.get_course_data()
            if command == "3":
                self.statistics()
            else:
                self.help()

application = courseRecordsApplication()
application.execute()
