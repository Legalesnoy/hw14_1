from abc import ABC


class PrintMixin:
    def __init__(self):
        print(f"{repr(self)}")


    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"('{self.name}', '{self.description}', "
                f"{self.price}, {self.quantity})")
