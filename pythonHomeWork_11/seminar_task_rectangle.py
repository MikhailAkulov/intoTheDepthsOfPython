# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.
# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

class Rectangle:
    """Класс Прямоугольник. Содержит параметры "длина" и "ширина", вычисляет периметр и площадь."""
    def __init__(self, length: int | float, width=0):
        self.length = length
        if not width:
            width = length
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
        perimeter = max(self.get_perimetr(), other.get_perimetr()) - min(self.get_perimetr(), other.get_perimetr())
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
    rect = Rectangle(10, 5)
    print(f'Периметр прямоугольника =  {rect.get_perimetr()}')
    print(f'Площадь прямоугольника = {rect.get_area()}')

    square = Rectangle(15)
    print(f'Периметр квадрата = {square.get_perimetr()}')
    print(f'Площадь квадарата = {square.get_area()}')
