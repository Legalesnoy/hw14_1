import pytest

from src.product import Info, Product, Category

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
def category1():
    return Category("Телевизоры",
                         "Синий",
                    [product1, product2, product3]
                    )