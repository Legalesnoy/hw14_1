from src.base_product import BaseProduct


class Info(BaseProduct):
    """ базовый класс для определения имени и описания категории или товара"""
    name: str
    description: str

    def __init__(self, name, description):
        self.name = name
        self.description = description
        super().__init__()

    def __str__(self):
        return self.name

    def new_product(self, product):
        pass
