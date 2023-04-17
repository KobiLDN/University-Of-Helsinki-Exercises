# Write your solution here
def shortest(spiderman):
    shortest = 100
    shortest_name = ""
    for name in spiderman:
        if len(name) <= shortest:
            #print(name)
            shortest = len(name)
            shortest_name = name
    return shortest_name


if __name__ == "__main__":
    my_list = ["eleventh", "first", "second", "fourth"]
    result = shortest(my_list)
    print(result)