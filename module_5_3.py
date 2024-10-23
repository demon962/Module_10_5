class House:
    def __init__(self, floors):
        self.floors = floors

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors

    def add(self, value):
        self.floors += value
        return self

    def radd(self, value):
        return self.add(value)

    def __iadd__(self, value):
        return self.add(value)

    def __str__(self):
        return f"House with {self.floors} floors."


house1 = House(3)
house2 = House(5)

print(house1 == house2)
print(house1 < house2)
print(house1 <= house2)
print(house1 > house2)
print(house1 >= house2)
print(house1 != house2)

house1.add(2)
print(house1)

house1 += 1
print(house1)