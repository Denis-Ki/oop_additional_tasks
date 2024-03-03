"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError(f"Index {index} out of range")


# код для проверки
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print(my_list[2])  # 2
