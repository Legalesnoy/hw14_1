import pytest

from src.lawn_grass import LawnGrass
from src.product import Info, Product
from src.category import Category, ProductIterator
from src.smartphone import Smartphone


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


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

@pytest.fixture
def category_without_prod_lst():
    return Category("XXX",
                    "XXX",
                    []
                    )
