def oldest_person(people: list):
    list_of_ages = ()
    helper = 0 # keeps track of oldest person
    for name, yob in people:
        age = 2023 - yob
        if age >= helper:
            helper = age
            nameofdionsaur = name
    return nameofdionsaur

if __name__ == "__main__":
    
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    
    print(oldest_person(people))