# Задание 2.
# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
from __future__ import annotations


class NegativeValueError(Exception):
    def __init__(self, value: int | float):
        self.value = value

    def __str__(self):
        return f"Нельзя создавать прямоугольник со сторонами отрицательной длины: {self.value}"


class SubtractionError(Exception):
    def __str__(self):
        return f"При вычитании большего из меньшего, результат будет отрицательным."


class Rectangle:
    """Класс Прямоугольник. Содержит параметры "длина" и "ширина", вычисляет периметр и площадь."""
    def __init__(self, length: int | float, width: int | float = None):
        self.length = length
        if not width:
            width = length
        if length < 0:
            raise NegativeValueError(length)
        elif width < 0:
            raise NegativeValueError(width)
        self.width = width

    def get_perimetr(self) -> int | float:
        """Функция возвращает периметр четырёхугольника"""
        return 2 * self.length + 2 * self.width

    def get_area(self) -> int | float:
        """Функция возвращает площадь четырёхугольника"""
        return self.length * self.width

    def __add__(self, other):
        perimeter = self.get_perimetr() + other.get_perimetr()
        return Rectangle(perimeter / 4)

    def __sub__(self, other):
        perimeter = self.get_perimetr() - other.get_perimetr()
        if perimeter < 0:
            raise SubtractionError()
        return Rectangle(perimeter / 4)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __str__(self):
        return f'length = {self.length}; width = {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width}'


if __name__ == '__main__':
    # rect1 = Rectangle(10, 5)
    # print(f'Периметр прямоугольника =  {rect1.get_perimetr()}')
    # print(f'Площадь прямоугольника = {rect1.get_area()}')
    #
    # square = Rectangle(15)
    # print(f'Периметр квадрата = {square.get_perimetr()}')
    # print(f'Площадь квадарата = {square.get_area()}')

    rect2 = Rectangle(7, 12)
    rect3 = Rectangle(16, 8)
    res1 = rect3 - rect2
    res2 = rect2 - rect3
