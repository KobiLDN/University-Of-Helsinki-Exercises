class Present:

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:

    def __init__(self):
        self.presentsList = []

    def add_present(self, present: Present):
        self.presentsList.append(present)

    def total_weight(self):        
        sum_weight = 0
        for present in self.presentsList:
            sum_weight += present.weight
        return sum_weight