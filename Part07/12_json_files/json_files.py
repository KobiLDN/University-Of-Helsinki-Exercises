import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person["name"]
        age = person["age"]
        hobbies = ", ".join(person["hobbies"])
        print(f"{name} {age} years ({hobbies})")


if __name__ == "__main__":
    filename = "file1.json" #input("filename ")
    print_persons(filename)