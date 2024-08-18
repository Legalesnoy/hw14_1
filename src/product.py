class Info:
    """ базовый класс для определения имени и описания категории или товара"""
    name: str
    description: str

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


class Product(Info):
    """товары"""
    __price: float = 0
    quantity: int = 0

    def __init__(self, name, description, price, quantity):
        Info.__init__(self, name, description)
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """полная стоимость всех товаров на складе"""
        return self.quantity * self.__price + other.quantity * other.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):

        if new_price > 0:

            if self.__price > new_price:
                if input("Понижаем цену? да - 'y', нет - 'n'\n") == 'y':
                    self.__price = round(new_price, 2)
            else:
                self.__price = round(new_price, 2)

        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product):
        name = product['name']
        description = product.get('description', '')
        price = product.get('price', 0)
        quantity = product.get('quantity', 0)
        return cls(name, description, price, quantity)


def merge_product(products: list[Product], product: Product):
    for el in products:
        if el.name == product.name:
            el.quantity += product.quantity
            el.price = max(el.price, product.price)
            break
    products.append(product)
    return products


class Category(Info):
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        Info.__init__(self, name, description)
        self.__products = products if products else []
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self):
        sum_prod = sum([p.quantity for p in self.__products])
        return f'Категория {self.name}, количество продуктов: {sum_prod} шт.'

    @property
    def product_list(self):
        prod_lst_str = ""
        for prod in self.__products:
            prod_lst_str += f'{str(prod)}\n'
        return prod_lst_str

    def add_product(self, product: Product):

        self.__products.append(product)
        Category.product_count += 1


class ProductIterator:
    """ класс для перебора продуктов в категории """
    index = 0
    def __init__(self, user_category):
        self.category = user_category


    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        prod_list = self.category.product_list.split('\n')
        if self.index < len(prod_list):
            prod = prod_list[self.index]
            self.index += 1
            return prod
        else:
            # self.index = 0
            raise StopIteration

if __name__ == "__main__":
    apple = Product("Яблоко", "Голден", 59.99, 50)
    print(apple)
    apple_dict = {'name': "Яблоко", 'description': "Голден", 'price': 50.99, 'quantity': 100}
    apple1 = Product.new_product(apple_dict)
    # # print(Product.new_product(apple_dict).name)
    #
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1+product2)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    p = [product1, product2, product3, apple]
    # print(apple.name, apple.description, apple.price, apple.quantity)
    #
    print(category1.product_list)
    print(category1)

    # category1.add_product(apple)
    # print('\n')
    # print(category1.product_list)
    # print(category1.product_count)
    category2 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2])
    print(category1.product_count)
    iterator = ProductIterator(category1)
    for product in iterator:
        print(product)
    for product in iterator:
        print(product)
    # print(f"c2_product_count {category2.product_count}")
    # print(f"c1_product_count {category1.product_count}")
    # # merge_product(p, apple1)
    # apple1.price = 33
    # print(apple1.__dict__)
    # print(p[3].__dict__)
    # print(category1.name == "Смартфоны")
    # print(category1.description)
    # #
    # # # print(len(category1.products))
    # print(category1.category_count)
    # print(category1.product_count)
    # #
    # product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    # category2 = Category(
    #      "Телевизоры",
    #      "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    #      [product4],
    # )
    # #
    # print(category2.name)
    # print(category2.description)
    # # # print(len(category2.products))
    # # # print(category2.products)
    # #
    # print(Category.category_count)
    # print(Category.product_count)
