from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra",
            "256GB",
            180000.0,
            5)
    message1 = capsys.readouterr()
    assert message1.out.strip() == "Product('Samsung Galaxy S23 Ultra', '256GB', 180000.0, 5)"

    Smartphone("Samsung Galaxy S23 Ultra", '256GB', 180000.0, 5)
    message2 = capsys.readouterr()
    assert message2.out.strip() == "Smartphone('Samsung Galaxy S23 Ultra', '256GB', 180000.0, 5)"

    LawnGrass("клевер", "Трава для газона", 150, 52, "Россия", "7 дней", "Зеленый")
    message3 = capsys.readouterr()
    assert message3.out.strip() == "LawnGrass('клевер', 'Трава для газона', 150, 52)"