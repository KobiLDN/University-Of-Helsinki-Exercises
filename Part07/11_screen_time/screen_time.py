from datetime import datetime, timedelta

def main():
    filename = input("Filename: ")
    starting_date = str(input("Starting date: "))
    how_many_days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile):")

    starting_date = datetime.strptime(starting_date, "%d.%m.%Y")
    end_date = (starting_date + timedelta(days=how_many_days-1))
    with open(filename, "w") as file:
        file.write("Time period: "+starting_date.strftime("%d.%m.%Y")+"-"+str(end_date.strftime("%d.%m.%Y")))
        file.write("\n")
    sum = 0
    screenTimeList = []
    for i in range(how_many_days):
        screenTime = str(input("Screen time " + starting_date.strftime("%d.%m.%Y") + ": "))
        y = starting_date.strftime("%d.%m.%Y")
        screenTimeList.append(datesAndMinutes(screenTime, y))
        screenTime = screenTime.split(" ")
        x = screen_time_sum(screenTime)
        sum += x
        starting_date += timedelta(days=1)

    with open(filename, "a") as file:
        file.write("Total minutes: " + str(sum)+"\n")
        file.write("Average minutes: " + str(sum / how_many_days)+"\n")
        for dates in screenTimeList:
            file.write(dates+"\n")
    print("Data stored in file " + filename)

def screen_time_sum(screentime):
    sum = 0
    for i in screentime:
        sum += int(i)
    return sum

def datesAndMinutes(screenTime, starting_date):
    screentimeListSTR = ""
    screentimeListSTR += starting_date + ": "
    screentimeListSTR += screenTime.replace(" ", "/")
    return screentimeListSTR


main()