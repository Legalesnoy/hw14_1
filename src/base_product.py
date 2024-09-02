from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """базовый класс для класса товары"""

    @abstractmethod
    def new_product(self, product):
        pass
