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