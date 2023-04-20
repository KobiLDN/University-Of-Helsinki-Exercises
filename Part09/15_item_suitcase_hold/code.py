class Item:

    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:

    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcaseList = []

    def weight(self):
        self.__weightSum = 0
        for item in self.__suitcaseList:
            self.__weightSum += item.weight()
        return self.__weightSum

    def add_item(self, new_item: Item):
        if new_item.weight() + self.weight() <= self.__max_weight:
            self.__suitcaseList.append(new_item)

    def __str__(self):
        if len(self.__suitcaseList) == 1:
            return f"{len(self.__suitcaseList)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__suitcaseList)} items ({self.weight()} kg)"

    def print_items(self):
        for items in self.__suitcaseList:
            print(f"{items}")


    def heaviest_item(self):
        heaviest_item = 0
        if len(self.__suitcaseList) >= 0:
            for item in self.__suitcaseList:
                if item.weight() > heaviest_item:
                    heaviest_item = item.weight()
            for item in self.__suitcaseList:
                if heaviest_item == item.weight():
                    return item
        else:
            return None


class CargoHold:

    def __init__(self, max_weight: int):
        self.__cargo_max_weight = max_weight
        self.__cargoList = []

    def cargo_weight(self):
        self.__cargoSumWeight = 0
        for suitcase in self.__cargoList:
            self.__cargoSumWeight += suitcase.weight()
        return self.__cargoSumWeight

    def add_suitcase(self, suitcase: Suitcase):
        if self.cargo_weight() + suitcase.weight() <= self.__cargo_max_weight:
            self.__cargoList.append(suitcase)
        else:
            return

    def __str__(self):
        if len(self.__cargoList) == 1:
            return f"{len(self.__cargoList)} suitcase, space for {self.__cargo_max_weight - self.cargo_weight()} kg"
        return f"{len(self.__cargoList)} suitcases, space for {self.__cargo_max_weight - self.cargo_weight()} kg"

    def print_items(self):
        for i in self.__cargoList:
            i.print_items()
            # for item in suitcase._Suitcase__suitcaseList:
            #     print(f"{item.name()} ({item.weight()} kg)")

