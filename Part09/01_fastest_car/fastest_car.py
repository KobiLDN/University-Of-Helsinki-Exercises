class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars: list):
    fastest_carMake = cars[0].make
    fastest_carSpeed = cars[0].top_speed

    for car in cars:
        if car.top_speed > fastest_carSpeed:
            fastest_carMake = car.make
            fastest_carSpeed = car.top_speed
    return fastest_carMake


if __name__ == "__main__":
    car1 = Car("Mercedes-Benz", 200)
    car2 = Car("Lada", 100)

    cars = [car1, car2]
    print(fastest_car(cars))
