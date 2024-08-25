class Info:
    """ базовый класс для определения имени и описания категории или товара"""
    name: str
    description: str

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name