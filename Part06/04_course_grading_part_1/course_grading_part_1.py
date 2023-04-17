student_file = str(input("Student information: "))
exercise_file = str(input("Exercises completed: "))
# name is first name space surname space total number of exercises completed  "pekka peloton 21"


student_dict = {}

def students():
    with open(student_file) as stud_file:
        for row in stud_file:
            row = row.replace("\n", "")
            parts = row.split(";")
            if parts[0] == "id":
                continue
            #dict[key] = value
            student_dict[parts[0]] = f"{parts[1]} {parts[2]}"
    return student_dict

exercise_dict = {}
def exercises_completed():
    #exercise_dict = {}
    with open(exercise_file) as exe_file:
        for row in exe_file:
            row = row.replace("\n", "")
            parts = row.split(";")
            if parts[0] == "id":
                continue
            #dict[key] = value
            exercise_dict[parts[0]] = parts[1:]
    return exercise_dict

def student_info():

    for id, name in student_dict.items():
        if id in exercise_dict:
            value = exercise_dict[id]
            ex_sum = 0
            for i in value:
                ex_sum += int(i)
            print(f"{name} {ex_sum}")
            #print(value)
        else:
            print(f"Not in database")
        #value = exercise_dict.get(id)
        #print(f"{name} {len(value)}")
students()
exercises_completed()
student_info()