# var that takes 2 sets of number into a list?
# Exam points are integers between 0 and 20.
# The number of exercises completed is an integer between 0 and 100.
# empty line = return

def main(results):
    total_points = []
    results = []
    passpercentlist = []
    while results != "":
        results = input("Exam points and exercises completed: ")
        if results == "":
            break
        results = results.split()
        xExam = int(results[0])
        yExercise = int(results[1])
        if xExam > 20 or yExercise > 100:
            print("exam points only between 0 - 20")
            print("exercise points only between 0 - 100")
            continue
        else:
            if xExam < 10 or xExam + (exercise_pointsCalc(yExercise)) <= 14:
                passpercentlist.append(0)
                yExercise = (exercise_pointsCalc(yExercise))
                total_points.append(xExam + yExercise)
            else:
                yExercise = (exercise_pointsCalc(yExercise))
                total_points.append(xExam + yExercise)
                passpercentlist.append(xExam + yExercise)
    #return total_points
    print("Statistics:")
    print(f"Points average: {points_average(total_points)}")
    print(f"Pass percentage: {pass_percentage(passpercentlist):.1f}")
    return passpercentlist

def exercise_pointsCalc(exercises_completed):
    return exercises_completed // 10

def points_average(total_points):

    average_points = 0
    for average in total_points:
        average_points += average
    return average_points / len(total_points)
    #print(f"Points average: {average_points} ")

def pass_percentage(totalpercent):
    passPercentage = 0
    for item in totalpercent:
        if item > 0:
            item = 1
            passPercentage += item
    passPercentage = (passPercentage / len(totalpercent)) * 100
    return passPercentage
    #print(f"Pass percentage {passPercentage}")

def grade_distribution(totalpoints):
    grade0 = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    star = "*"
    for item in totalpoints:
        if item >= 0 and item <= 14:
            grade0 += 1
        elif item >= 15 and item <= 17:
            grade1 += 1
        elif item >= 18 and item <= 20:
            grade2 += 1
        elif item >= 21 and item <= 23:
            grade3 += 1
        elif item >= 24 and item <= 27:
            grade4 += 1
        elif item >= 28 and item <= 30:
            grade5 += 1

    print("Grade distribution:")
    print("5:", star * grade5)
    print("4:", star * grade4)
    print("3:", star * grade3)
    print("2:", star * grade2)
    print("1:", star * grade1)
    print("0:", star * grade0)

percents = main(0)
grade_distribution(percents)