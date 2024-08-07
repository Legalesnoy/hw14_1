class Info:
    name: str
    description: str

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Product(Info):
    price: float = 0
    quantity: int = 0

    def __init__(self, name, description, price, quantity):
        Info.__init__(self, name, description)
        self.price = price
        self.quantity = quantity


class Category(Info):
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        Info.__init__(self, name, description)
        self.products = products if products else []
        self.product_count = len(products)
        Category.category_count += 1


if __name__ == "__main__":
    apple = Product("Яблоко", "Голден", 59.99, 50)
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(apple.name, apple.description, apple.price, apple.quantity)

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
