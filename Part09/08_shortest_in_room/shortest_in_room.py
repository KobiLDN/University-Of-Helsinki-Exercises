# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:

    def __init__(self):
        self.list_of_persons = []
        self.heightList = []

    def add(self, person: Person):
        self.list_of_persons.append(person)
        self.heightList.append(person.height)

    def is_empty(self):
        return len(self.list_of_persons) == 0

    def print_contents(self):
        if len(self.list_of_persons) == 0:
            return f"There are no people"
        else:
            print(f"There are {len(self.list_of_persons)} persons in the room, and their combined height is {sum(self.heightList)} cm")
            for i in self.list_of_persons:
                print(f"{i} ({i.height} cm)")

    def shortest(self):
        if len(self.list_of_persons) == 0:
            return None
        else:
            for person in self.list_of_persons:
                if person.height == sorted(self.heightList)[0]:
                    return person

    def remove_shortest(self):
        if len(self.list_of_persons) == 0:
            return None
        else:
            shortest_person = self.shortest()
            shortest_height = shortest_person.height
            self.list_of_persons.remove(shortest_person)
            self.heightList.remove(shortest_height)
            return shortest_person

        # else:
        #     self.heightList.sort()
        #     count = -1
        #     for person in self.list_of_persons:
        #         count += 1
        #         if person.height == self.heightList[0]:
        #             self.list_of_persons.pop(count)
        #             self.heightList.pop(0)
        #             return person