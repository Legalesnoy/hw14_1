from src.order import Order


def test_order_init(product1):
    order1 = Order.new_product(product1)
    assert order1.name == "Samsung Galaxy S23 Ultra"
    assert order1.price == 180000.0
    assert order1.quantity == 5
    assert order1.description == ""


def test_order_new_product(product1):
    order1 = Order.new_product(product1)
    assert order1.name == "Samsung Galaxy S23 Ultra"
    assert order1.price == 180000.0
    assert order1.quantity == 5
    assert order1.description == ""

def test_order_str(product1):
    order1 = Order.new_product(product1)
    assert order1.__str__() == "Куплен товар 'Samsung Galaxy S23 Ultra', за 180000.0 руб.,количество купленного товара 5 шт."