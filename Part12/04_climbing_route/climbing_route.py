class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


# Write your solution herer:
def sort_by_length(routes: list):
    def order_by_length(route: list):
        return route.length

    return sorted(routes, key=order_by_length, reverse=True)


def sort_by_difficulty(routes: list):
    def order_by_difficulty(route: list):
        return route.grade, route.length

    return sorted(routes, key=order_by_difficulty, reverse=True)

if __name__ == "__main__":
    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    r4 = ClimbingRoute("Smooth operator", 9, "7A")
    r5 = ClimbingRoute("Syncro", 14, "8C+")

    routes = [r1, r2, r3, r4, r5]
    for route in sort_by_difficulty(routes):
        print(route)
