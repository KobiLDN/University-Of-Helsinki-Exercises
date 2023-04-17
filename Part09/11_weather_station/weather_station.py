class WeatherStation:

    def __init__(self, name: str):
        self.__latest_observation = ""
        self.__name = name
        self.__count = 0

    def add_observation(self, observation: str):
        if observation != "":
            self.__count += 1
            self.__latest_observation = observation
        else:
            raise ValueError("observation must not be empty")

    def latest_observation(self):
        if self.__latest_observation == "":
                return ""
        else:
            return self.__latest_observation

    def number_of_observations(self):
        if self.__count > 0:
            return self.__count
        else:
            return 0

    def __str__(self):
        return f"{self.__name}, {self.__count} observations"

