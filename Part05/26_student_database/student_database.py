def add_student(batman: dict, persons: str):
    batman[persons] = ()

def print_student(batman: dict, persons: str,):
    if persons not in batman:
        print(f"{persons}: no such person in the database")
    elif len(batman[persons]) == 0:
        print(persons, ":", sep="")
        print(" no completed courses")
    else:
        print(persons, ":", sep="")
        course_count = len(batman[persons])
        print(f" {course_count} completed courses:")
        for course, grade in batman[persons]:
            print(" ", course, grade[0])
        sum = 0
        for course, grade in batman[persons]:
            sum += grade[0]
        print(" average grade", sum / course_count)

def add_course(batman: dict, persons: str, course: tuple):
        newcourse_name, newcourse_grade = course
        if newcourse_grade == 0:
            return
        if len(batman[persons]) == 0:
            batman[persons] += (newcourse_name, [newcourse_grade]),
            #print(batman[persons])
            return
        for currentCourse, currentGrade in batman[persons]:
            if currentCourse == newcourse_name: # if the course grade is more
                #print("matches course")
                if currentGrade[0] < newcourse_grade:
                    currentGrade[0] = newcourse_grade
                    #print("current grade is less")
                    return
                if currentGrade[0] > newcourse_grade:
                    #print("current grade is more")
                    return
            else:
                #print("doesn't match")
                batman[persons] += (newcourse_name, [newcourse_grade]),
                return
        #print(batman[persons])

def summary(batman: dict):
    print("students", len(batman))

    mostCoursesCompleted = 0
    name = ""
    for person, coursesGrade in batman.items():
        # print(person)
        coursesCompleted = 0
        for courses, grades in coursesGrade:
            coursesCompleted += 1
            # print(courses, grades[0])
            if coursesCompleted > mostCoursesCompleted:
                mostCoursesCompleted = coursesCompleted
                name = person
        # print(coursesCompleted)
    print("most courses completed", mostCoursesCompleted, name)

    courseName = ""
    currentGrade = 0
    name = ""
    bestAverageGrade = 0
    for person, coursesGrade in batman.items():
        # print(person)
        gradeSum = 0
        gradeCount = 0
        for courses, grades in coursesGrade:
            if courses == courseName:
                if grades[0] < currentGrade:
                    print("return")
                    continue
            currentGrade = grades[0]
            courseName = courses
            gradeCount += 1
            gradeSum += grades[0]
            gradeAverage = gradeSum / gradeCount
            if gradeAverage > bestAverageGrade:
                bestAverageGrade = gradeSum / gradeCount
                name = person

    print("best average grade", bestAverageGrade, name)

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)