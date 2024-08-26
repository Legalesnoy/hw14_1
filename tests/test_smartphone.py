def test_smartphone(smartphone1):
   assert smartphone1.__str__() == ('Samsung Galaxy S23 Ultra, '
                                    '180000.0 руб. '
                                    'Остаток: 5 шт. '
                                    'производительность: 95.5, '
                                    'модель: S23 Ultra, '
                                    'объем встроенной памяти: 256, '
                                    'цвет: Серый')