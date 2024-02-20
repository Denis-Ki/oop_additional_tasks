# Реализуйте два метода from_string и is_date_valid.
# Метод from_string создает и инициализирует экземпляр Date из переданной строки.
# Метод is_date_valid проверяет, корректные ли формат и значение строки переданы.

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = date_str.split('-')
        return cls(int(day), int(month), int(year))

    @staticmethod
    def is_date_valid(date_str):
        date = Date.from_string(date_str)
        if date.day > 31:
            return False
        elif date.month > 12:
            return False
        else:
            return True



date = Date.from_string('23-09-2022')
print(date.day)
# 23
print(date.month)
# 9
print(date.year)
# 2022
print(Date.is_date_valid('23-09-2022'))
# True
print(Date.is_date_valid('23-15-2022'))  # месяц
# False
print(Date.is_date_valid('32-09-2022'))  # день
# False
