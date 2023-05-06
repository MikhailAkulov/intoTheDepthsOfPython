# Задание №1
# 📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.
from __future__ import annotations


def set_number() -> int | float:
    while True:
        a = input('Введите целое или вещественное число: ')
        try:
            number = int(a)
            return f'Вы ввели: {number}'
        except ValueError:
            try:
                number = float(a)
                return number
            except ValueError as e:
                print(f'Ошибка ввода - {e}, попробуйте ещё')


if __name__ == '__main__':
    print(set_number())
