import pytest

from src.product import Info, Product, Category, ProductIterator


@pytest.fixture
def info1():
    return Info("Яблоко",
                "Голден")


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB",
                   180000.0,
                   5)


@pytest.fixture
def product2():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11",
                   "1024GB, Синий",
                   31000.0,
                   14)


@pytest.fixture
def category1(product1, product2, product3):
    return Category("Телевизоры",
                    "Синий",
                    [product1, product2, product3]
                    )


@pytest.fixture
def category2(product1, product2):
    return Category("Телевизоры",
                    "Синий",
                    [product1, product2]
                    )

@pytest.fixture
def price1():
    return 9999999999


@pytest.fixture
def prod_lst1(product1, product2, product3):
    return [product1, product2, product3]


@pytest.fixture
def prod_lst2(product1, product2):
    return [product1, product2]


@pytest.fixture
def prod_lst_str():
    return 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'

@pytest.fixture
def product_iterator(category1):
    return ProductIterator(category1)
