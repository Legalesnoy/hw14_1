import pytest


def test_lawn_grass(grass1):
    assert grass1.__str__() == ("Газонная трава, 500.0 руб. Остаток: 20 шт., "
                                "страна-производитель: Россия, "
                                "срок прорастания: 7 дней, "
                                "цвет: зеленый")


def test_lawn_grass_add(grass1, grass2):
    grass_sum = grass1 + grass2
    assert grass_sum == 16750.0


def test_lawn_grass_add_error(grass1, smartphone1):
    with pytest.raises(TypeError):
        _ = grass1 + 1

    with pytest.raises(TypeError):
        _ = grass1 + smartphone1
