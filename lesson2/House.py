# Реализуйте класс House с одним защищенным атрибутом — цена.
# # Добейтесь следующего поведения от этого класса:
# >>> house = House(50000.0)
#
# >>> house.price
# 50000.0
#
# >>> house.price = 45000.0  # обновили значение
# >>> house.price
# 45000.0
#
# >>> house.price = -50
# Пожалуйста, введите корректное значение
#
# >>> house.price
# 45000.0
#
# >>> del house.price
# >>> house.price
# AttributeError: 'House' object has no attribute '_price'.

class House():
    price: float

    def __init__(self, price):