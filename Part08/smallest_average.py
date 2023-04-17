def smallest_average(person1: dict, person2: dict, person3: dict):
    dictionary = [person1, person2, person3]
    sum1 = 0
    average = 9
    name = ""
    count = 0
    dict1 = {}
    for i in dictionary:
        for key, value in i.items():
            if key == "name":
                sum1 = 0
                count = 0
                continue
            count += 1
            sum1 += value
        if (sum1 / count) < average:
            average = sum1 / count
            dict1 = i
            name = i["name"]
    return dict1



if __name__ == "__main__":
    person1 = {"name": "Anna", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Anna", "result1": 8, "result2": 8, "result3": 8}
    person3 = {"name": "Anna", "result1": 7, "result2": 7, "result3": 7}

    print(smallest_average(person1, person2, person3))