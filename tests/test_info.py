def test_info_init(info1):
    assert info1.name == "Яблоко"
    assert info1.description == "Голден"


def test_info_str(info1):
    assert str(info1) == 'Яблоко'
