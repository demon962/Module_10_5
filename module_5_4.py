class House:
    houses_history = []
    def __init__(self, *args):
        self.name = args[0]
        self.address = args[1]

    @classmethod
    def new(cls, *args):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return cls(*args)
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

if __name__ == "__main__":

    house1 = House.new('Дом1', 'ул. Прима')
    house2 = House.new('Дом2', 'ул. Секунда')
    house3 = House.new('Дом3', 'ул. Терция')

    print("История созданных домов:", House.houses_history)

    del house2

    print("История созданных домов после удаления:", House.houses_history)
