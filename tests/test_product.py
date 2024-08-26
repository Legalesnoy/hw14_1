from src.product import Product
import pytest


def test_product_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    assert product1.description == "256GB"


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
    assert product1.merge_product(prod_lst2, product3) == prod_lst1
    product1.price = price1
    product1.merge_product(prod_lst2, product1)
    assert prod_lst2[0].price == 9999999999


def test_product_str(product3):
    assert str(product3) == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.'


def test_product_add(product3, product1):
    assert product3 + product1 == 1_334_000.0


def test_product_iterator(product_iterator, product1, product2, product3):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator) == str(product1)
    assert next(product_iterator) == str(product2)
    assert next(product_iterator) == str(product3)

