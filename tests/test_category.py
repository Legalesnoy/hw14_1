import pytest


def test_category_init(category1):
    assert category1.name == "Телевизоры"
    assert category1.description == "Синий"
    assert category1.category_count == 1
    assert category1.product_count == 3


def test_category_property(category1, prod_lst_str):
    assert category1.products == prod_lst_str


def test_category_add_product(category1, category2, product3, prod_lst_str):
    category2.add_product(product3)
    assert category2.products == prod_lst_str


def test_category_add_product_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(1)


def test_category_str(category1):
    assert str(category1) == 'Категория Телевизоры, количество продуктов: 27 шт.'
