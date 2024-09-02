from src.base_product import BaseProduct
from src.info import Info
from src.product import Product


class Order(Info):
    """Класс «Заказ» содержит какой товар был куплен,
       В заказе может быть указан только один товар. """

    def __init__(self, product: Product, description: str = ''):
        self.price = product.price
        self.quantity = product.quantity
        super().__init__(product.name, description)

    def __str__(self):

        if self.description:
            comment = f"\nКомменетрий к заказу: {self.description}"
        else:
            comment = ""
        return (f"Куплен товар '{self.name}', за {self.price} руб.,"
                f"количество купленного товара {self.quantity} шт.{comment}"
                )

    @classmethod
    def new_product(cls, product: Product):
        return cls(product)


if __name__ == "__main__":
    apple = Product("Яблоко", "Голден", 59.99, 50)
    order1 = Order.new_product(apple)
    order2 = Order(apple)
    print(order2)
