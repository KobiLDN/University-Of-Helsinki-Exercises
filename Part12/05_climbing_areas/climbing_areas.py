class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"

def sort_by_number_of_routes(areas: list):
    def order_by_routes(items: list):
        return items.routes()
    return sorted(areas, key=order_by_routes)

def sort_by_most_difficult(areas: list):

    def order_by_hardest(items: list):
        #print(items)
        return items.hardest_route().grade

    return sorted(areas, key=order_by_hardest, reverse=True)


if __name__ == "__main__":
    k1 = ClimbingArea("Area 53")
    k1.add_route(ClimbingRoute("Edge", 38, "6A+"))
    k1.add_route(ClimbingRoute("Big cut", 36, "6B"))
    k1.add_route(ClimbingRoute("The Swedish route", 42, "5+"))

    k2 = ClimbingArea("Moor")
    k2.add_route(ClimbingRoute("Syncro", 14, "8C+"))

    k3 = ClimbingArea("Climbstation")
    k3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
    k3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
    k3.add_route(ClimbingRoute("No grip", 12, "6B+"))
    k3.add_route(ClimbingRoute("Fruit garden", 8, "6A"))

    # print(ca1)
    # print(ca3.name, ca3.routes())
    # print(ca3.hardest_route())

    # ca1, ca2 and ca3 declared as above
    areas = [k1, k2, k3]
    for area in sort_by_most_difficult(areas):
        print(area)