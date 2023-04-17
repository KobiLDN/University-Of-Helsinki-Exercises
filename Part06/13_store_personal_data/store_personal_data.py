# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as peeps:
        person1 = f"{person[0]};{person[1]};{person[2]}"
        peeps.write(person1 + "\n")

if __name__ == "__main__":
    person = ("Paul Paulson", 37, 175.5)
    store_personal_data(person)