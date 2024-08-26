from src.product import Product


class Smartphone(Product):
    """ класс смартфон"""

    def __init__(self, name, description, price, quantity, efficiency="", model="", memory="", color=""):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объем встроенной памяти
        self.color = color  # цвет

    def __str__(self):
        return f'{super().__str__()} производительность: {self.efficiency}, модель: {self.model}, объем встроенной памяти: {self.memory}, цвет: {self.color}'


if __name__ == "__main__":
    samsung = Smartphone("Samsung Galaxy S23 Ultra", "", 180000.0, 5)
    xiaomi = Smartphone("Xiaomi Redmi Note 11", "", 31000.0, 14)
    print(samsung)
