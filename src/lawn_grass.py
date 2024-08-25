from src.product import Product
from src.smartphone import Smartphone


class LawnGrass(Product):
    """класс Трава газонная"""
    def __init__(self, name, description, price, quantity, country="", germination_period="", color=""):
        super().__init__(name,description,price,quantity)
        self.country = country                         # страна-производитель
        self.germination_period = germination_period   # срок прорастания
        self.color = color                             # цвет

    def __str__(self):
        return f'{super().__str__()}, страна-производитель: {self.country}, срок прорастания: {self.germination_period}, цвет: {self.color.lower()}'


if __name__ == '__main__':
    clever = LawnGrass("клевер","Трава для газона",150,52,"Россия", "7 дней", "Зеленый")
    print(clever)
    samsung = Smartphone("Samsung Galaxy S23 Ultra","",180000.0,5,"","","","")
    xiaomi = Smartphone("Xiaomi Redmi Note 11","",31000.0,14,"","","","")
    # print(xiaomi+clever)
