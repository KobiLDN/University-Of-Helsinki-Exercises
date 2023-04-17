class Recording:
    def __init__(self, __length: int):
        if __length < 0:
            raise ValueError("The amount must not be below zero")
        else:
            self.__length = __length


    # a getter method
    @property
    def length(self):
        return self.__length

    # a setter method
    @length.setter
    def length(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The amount must not be below zero")

