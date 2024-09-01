from src.base_product import BaseProduct
from src.info import Info
from src.product import Product


class Category(BaseProduct):
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
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def new_product(self, product: Product):
        self.add_product(product)


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
