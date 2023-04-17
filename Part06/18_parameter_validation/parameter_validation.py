def new_person(name: str, age: int):
    error = False
    if name == "":
        error = True
        raise ValueError("name is an empty string")
    if name.find(" ") == -1:
        error = True
        raise ValueError("name contains less than two words")
    if len(name) > 40:
        error = True
        raise ValueError("name is longer than 40 characters")
    if age < 0:
        error = True
        raise ValueError("age is a negative number")
    if age > 150:
        error = True
        raise ValueError("age is greater than 150")
    elif not error:
        return (name, age)
if __name__ == "__main__":
    new_person("john conner", 20)