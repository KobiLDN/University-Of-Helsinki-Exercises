import json
import urllib.request
from math import fsum

def retrieve_all():
    courses_list = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    courseslist = []
    # f = courses.read()
    # courses = json.loads(f)
    courses = json.loads(courses_list.read())
    # var = load jason (( read var))
    exercises_sum = 0
    for course in courses:
        if course["enabled"]:
            exercises_sum = 0
            fullName = course["fullName"]
            name = course["name"]
            year = course["year"]
            for i in course["exercises"]:
                exercises_sum += int(i)
            courseslist.append((fullName, name, year, exercises_sum))
    return courseslist

def retrieve_course(course_name: str):
    course = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/"+course_name+"/stats")
    course = json.loads(course.read())
    weeksCount = len(course.values())
    hours_sum = 0
    max_students = 0
    exercise_tot = 0
    for key in course.values():
        if key["students"] > max_students:
            max_students = key["students"]
        hours_sum += key["hour_total"]
        exercise_tot += key["exercise_total"]            

    return {
        "weeks": weeksCount,
        "students": max_students,
        "hours": hours_sum,
        "hours_average":  (hours_sum // max_students),
        "exercises": exercise_tot,
        "exercises_average" : exercise_tot // max_students,
    }

if __name__ == "__main__":
    courses_list = []
    y = retrieve_all()
    x = retrieve_course("ofs2019")
    print(x)