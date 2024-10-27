class House:
    houses_history = []

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.add_to_history(name)

    def add_to_history(self, name):
        House.houses_history.append(name)

    def delete(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __del__(self):
        self.delete()


if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)

    h2 = House('ЖК Акация', 20)
    print(House.houses_history)

    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)
    # Удаление объектов
    del h2
    del h3

    print(
        House.houses_history) 
