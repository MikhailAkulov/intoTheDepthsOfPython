# Задание 3.
# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ умножения матриц

class Matrix:
    """
    Класс Матрица содержит листы листов.
    Содержит методы печати, сравнения, сложения и умножения матриц.
    """
    def __init__(self, data: [[int | float]]):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            for el in row:
                result = f'{result} {el:>5}'
            result = f'{result}\n'
        return result

    def __repr__(self):
        result = ''
        for row in self.data:
            for el in row:
                result = f'{result} {el:>5}'
        return f'Matrix({result})'

    def __eq__(self, other):
        if len(self.data) == len(other.data) and len(self.data[0]) == len(other.data[0]):
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    if self.data[i][j] != other.data[i][j]:
                        return False
            return True
        return False

    def __add__(self, other):
        result = [[0] * len(self.data[0]) for _ in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result[i][j] = self.data[i][j] + other.data[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data) and len(other.data[0]) != len(self.data):
            return -1
        if len(other.data[0]) != len(self.data):
            a, b = other, self
        else:
            a, b = self, other
        result = [[0] * len(b.data[0]) for _ in range(len(a.data))]
        for i in range(len(a.data)):
            for j in range(len(b.data[0])):
                summa = 0
                for k in range(len(a.data[0])):
                    summa += a.data[i][k] * b.data[k][j]
                result[i][j] = summa
        return Matrix(result)


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'Матрица 1:\n{matrix1}')
    matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print(f'Матрица 2:\n{matrix2}')
    print(f'Результат сравнения матриц: {matrix1 == matrix2}\n')
    print(f'Результат сложения матриц:\n{matrix1 + matrix2}')
    print(f'Результат умножения матриц:\n{matrix1 * matrix2}')
