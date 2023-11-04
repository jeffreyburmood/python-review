""" this is a dynamic array (resizeable) """

class DynamicArray:

    def __init__(self, capacity):
        self.dymArray = []

        if capacity <= 0:
            self.capacity = 0
        else:
            self.capacity = capacity

    def get(self, i: int) -> int:
        return self.dymArray[i]

    def set(self, i: int, n: int) -> None:
        self.dymArray[i] = n

    def pushback(self, n: int) -> None:
        if len(self.dymArray) >= self.capacity:
            self.resize()
        self.dymArray.append(n)

    def popback(self) -> int:
        end = len(self.dymArray) - 1
        return self.dymArray.pop(end)

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.dymArray)

    def getCapacity(self) -> int:
        return self.capacity
