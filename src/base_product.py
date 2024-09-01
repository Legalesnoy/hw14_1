from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """базовый класс для класса товары"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        super().__init__()

    @abstractmethod
    def new_product(self, *a, **k):
        pass
