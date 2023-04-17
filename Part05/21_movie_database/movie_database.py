# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dict1 = {"name": "", "director": "", "year": 0, "runtime": 0}
    helper = database.copy()
    for i in range(1):
        dict1["name"] = name
        dict1["director"] = director
        dict1["year"] = year
        dict1["runtime"] = runtime
        database.append(dict1)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)