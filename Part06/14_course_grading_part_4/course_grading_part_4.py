exam_points_dict = {}

def exam_file_f():
    with open(exam_file) as exa_file:
        for row in exa_file:
            row = row.replace("\n", "")
            parts = row.split(";")
            if parts[0] == "id":
                continue
            exam_points_dict[parts[0]] = parts[1:]
    # print(exam_points_dict)
    return exam_points_dict


student_dict = {}


def students():
    with open(student_file) as stud_file:
        for row in stud_file:
            row = row.replace("\n", "")
            parts = row.split(";")
            if parts[0] == "id":
                continue
            # dict[key] = value
            student_dict[parts[0]] = f"{parts[1]} {parts[2]}"
    return student_dict


exercise_dict = {}


def exercises_completed():
    # exercise_dict = {}
    with open(exercise_file) as exe_file:
        for row in exe_file:
            row = row.replace("\n", "")
            parts = row.split(";")
            if parts[0] == "id":
                continue
            # dict[key] = value
            exercise_dict[parts[0]] = parts[1:]
    return exercise_dict


def student_info():
    with open("results.txt", "a") as results_file:
        string = ""
        print(course_info_f())
        titles = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
        for title in titles:
            if title == "name":
                print(f"{title:30}", end="")
                string += f"{title:30}"
                continue
            print(f"{title:10}", end="")
            string += f"{title:10}"
        results_file.write(string + "\n")
        string = ""
        print()

    for pic, name in student_dict.items():
        if pic in exam_points_dict:  # calc the exam points
            exam_points_dict_value = exam_points_dict[pic]
            exam_points_sum = 0
            for i in exam_points_dict_value:
                exam_points_sum += int(i)
            exam_points_dict_value = exam_points_sum
            # print(f"{name} {exam_points_dict_value}")

        if pic in exercise_dict:  # calc the exercises completed
            value = exercise_dict[pic]
            exercise_sum = 0
            for i in value:
                exercise_sum += int(i)
            exercise_sum_int = int((exercise_sum / 40) * 10)                 #calculate exercise points
            #print(f"{name} {exercise_sum}")                             #exec_nbr sum of exercise points
            #print(f"{name} {int(exercise_sum_int)}")                        #exec_pts exercise points
            #print(f"{name} {int(exam_points_dict_value+exercise_sum_int)}") #tot_pts
            grade = points_table(exam_points_dict_value+exercise_sum_int)   #calculate exm_pts
            string = f"{name:30}{exercise_sum:<10}{exercise_sum_int:<10}{exam_points_dict_value:<10}{(exam_points_dict_value+exercise_sum_int):<10}{grade:<10}"                                     #grade
            print(f"{name:30}{exercise_sum:<10}{exercise_sum_int:<10}{exam_points_dict_value:<10}{(exam_points_dict_value+exercise_sum_int):<10}{grade:<10}")                                        #grade
            with open("results.txt", "a") as results_file:
                results_file.write(string + "\n")
            with open("results.csv", "a") as results_csv:
                results_csv.write(f"{pic};{name};{grade} \n")
            # print(value)
        else:
            print(f"Not in database")

        # exercise_sum_value = exercise_dict.get(id)
        # print(f"{name} {len(exercise_sum_value)}")

def points_table(points):
    if points <= 14:
        grade = 0
    elif points <= 17:
        grade = 1
    elif points <= 20:
        grade = 2
    elif points <= 23:
        grade = 3
    elif points <= 27:
        grade = 4
    elif points >= 28:
        grade = 5
    return grade

def course_info_f():
    with open(course_info) as course_data:
        #line = ""
        course_info_list = []
        for course in course_data:
            course = course.replace("\n", "")
            parts = course.split(":")
            for i in parts:
                course_info_list.append(i.lstrip())
        line = f"{course_info_list[1]}, {course_info_list[3]} credits \n======================================"
    open("results.csv", 'w').close()
    with open("results.txt", "w") as results_file:
        results_file.write(line + "\n")
    return line


# student_file = str(input("Student information: "))
# exercise_file = str(input("Exercises completed: "))
# exam_file = str(input("Exam points: "))
# name is first name space surname space total number of exercises completed  "pekka peloton 21"
program = True
if program:
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = str(input("Exam points: "))
    course_info = str(input("Course information: "))
else:
    # now this is the False branch, and is never executed
    student_file = "students1.csv"
    exercise_file = "exercises1.csv"
    exam_file = "exam_points1.csv"
    course_info = "course1.txt"

course_info_f()
exam_file_f()
students()
exercises_completed()
student_info()