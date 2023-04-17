def read_fruits():
    dict1 = {}
    # dict[key] = value
    with open("fruits.csv") as new_file:
        for i in new_file:
            i = i.replace("\n","")
            #fruit = i.split(";")
            fruit, cost = i.split(";")
            dict1[fruit] = float(cost)
        # for fruit, cost in dict1.items():
        #     print(f"the cost of a {fruit} is {cost:.2f}")
    return dict1


if __name__ == "__main__":
    list1 = read_fruits()
    # for fruit, cost in list1.items():
    #     print(f"the cost of a {fruit} is {cost}")

