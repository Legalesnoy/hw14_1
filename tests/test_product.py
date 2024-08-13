from src.product import Product, merge_product, Category


def test_info_init(info1):
    assert info1.name == "Яблоко"
    assert info1.description == "Голден"


def test_product_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    assert product1.description == "256GB"


def test_category_init(category1):
    assert category1.name == "Телевизоры"
    assert category1.description == "Синий"
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_product_property(product1):
    assert product1.price == 180000.0


def test_product_setter(product1, price1):
    assert product1.price == 180000.0
    product1.price = price1
    assert product1.price == 9999999999


def test_product_new_product(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    assert product1.description == "256GB"


def test_merge_product(prod_lst2, product3, prod_lst1, product1, price1):
    assert merge_product(prod_lst2, product3) == prod_lst1
    product1.price = price1
    merge_product(prod_lst2, product1)
    assert prod_lst2[0].price == 9999999999


def test_category_property(category1, prod_lst_str):
    assert category1.product_list == prod_lst_str


def test_category_add_product(category1, category2, product3, prod_lst_str):
    category2.add_product(product3)
    assert category2.product_list == prod_lst_str
