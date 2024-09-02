from src.base_product import BaseProduct
from src.info import Info
from src.product import Product
from src.exception import ZeroQuantityProduct


class Category(Info):
    """класс для описания категории продукта"""
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        super().__init__(name, description)
        self.__products = products if products else []
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        sum_prod = sum([p.quantity for p in self.__products])
        return f'Категория {self.name}, количество продуктов: {sum_prod} шт.'

    @property
    def products(self):
        prod_lst_str = ""
        for prod in self.__products:
            prod_lst_str += f'{str(prod)}\n'
        return prod_lst_str

    def add_product(self, product: Product):
        if isinstance(product, Product):

            try:
                if product.quantity == 0:
                    raise ZeroQuantityProduct("Добавлять товар с нулевым количеством недопустимо")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print('Товар добавлен успешно')
            finally:
                print('Обработка добавления товара завершена')
        else:
            raise TypeError

    def new_product(self, product: Product):
        self.add_product(product)

    def average_cost(self):
        """метод, который подсчитывает средний ценник всех товаров."""
        try:
            return sum([p.quantity for p in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0



class ProductIterator:
    """ класс для перебора продуктов в категории """
    index = 0

    def __init__(self, user_category):
        self.category = user_category

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        prod_list = self.category.products.split('\n')
        if self.index < len(prod_list):
            prod = prod_list[self.index]
            self.index += 1
            return prod
        else:
            # self.index = 0
            raise StopIteration


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера",
                       180000.0,
                       5
                       )
    product2 = Product("Iphone 15",
                       "512GB, Gray space",
                       210000.0,
                       8)

    product3 = Product("Xiaomi Redmi Note 11",
                       "1024GB, Синий",
                       31000.0,
                       14)

    category1 = Category("Смартфоны",
                    "xxxx",
                    [product1, product2, product3])
    print(category1.average_cost())

    category2 = Category("xxxx",
                         "xxxx",
                         [])
    print(category2.average_cost())
    apple = Product("Яблоко", "Голден", 59.99, 50)
    apple.quantity = 0
    category2.add_product(apple)