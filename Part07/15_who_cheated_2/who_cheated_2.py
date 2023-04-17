import csv
from datetime import datetime, timedelta

def cheaters():
    not_cheaters = []
    with open("start_times.csv") as starts_file:
        startTimesList = csv.reader(starts_file, delimiter=";")
        startTimesList = list(startTimesList)

    with open("submissions.csv") as subs_file:
        subsList = csv.reader(subs_file, delimiter=";")
        subsList = list(subsList)

    cheaters = []
    for name, time in startTimesList:
        for name2, task, points, time2 in subsList:
            if name == name2:
                time_start = datetime.strptime(time, "%H:%M")
                time_end = datetime.strptime(time2, "%H:%M")
                duration = time_end - time_start
                if duration <= timedelta(hours=3):
                    x = (name, points, task)
                    not_cheaters.append(x)
                    continue
                if name in cheaters:
                    continue
                cheaters.append(name)
    return not_cheaters

def final_points():
    not_cheaters = cheaters()
    subs_dic = {}
    for name, points, task in not_cheaters:
        if name not in subs_dic: #  if name not in dict, add the person
            subs_dic[name] = {}
        if task not in subs_dic[name] or int(points) > subs_dic[name][task]: # name is key, task is the key, points is the value
            subs_dic[name][task] = int(points) # adds a nested dict called task
            # print(subs_dic[name][task]) task value
    #calculate points
    points_dict = {}
    for name, values in subs_dic.items():
        sum = 0
        for task, points in values.items():
            # print(task)
            # print(points)
            sum += int(points)
        points_dict[name] = sum
        # print(name)
        # print(values)
    return points_dict


if __name__ == "__main__":

    xxx = cheaters()
    result = final_points()
    print(result)
