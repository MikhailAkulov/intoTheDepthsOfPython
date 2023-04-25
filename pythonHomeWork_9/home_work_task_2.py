# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from typing import Callable
from random import randint as r
from functools import wraps

__all__ = ['square_calculation_func', 'gen_numbers_to_csv']


def convert_func_csv_to_json(func) -> Callable[[], None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        parameters = []
        with (
            open('source_homeworktask.csv', 'r', newline='') as f_csv,
            open('result_homeworktask.json', 'w') as f_json
        ):
            csv_file = csv.reader(f_csv)
            for row in csv_file:
                a, b, c = row
                result = func(int(a), int(b), int(c), *args, **kwargs)
                json_dict = {'a': a, 'b': b, 'c': c, 'result': result}
                parameters.append(json_dict)
            json.dump(parameters, f_json, ensure_ascii=False, indent=2)
    return wrapper


@convert_func_csv_to_json
def square_calculation_func(a: int, b: int, c: int) -> str:
    """Функция нахождения корней квадратного уравнения"""
    result = ''
    d = b ** 2 - 4 * a * c
    if d < 0:
        result = 'no roots'
    elif d == 0:
        x = (-b) / (2 * a)
        result = f'{x = }.'
    elif d > 0:
        x1 = ((-b) - d ** 0.5) / (2 * a)
        x2 = ((-b) + d ** 0.5) / (2 * a)
        result = f'{x1 = } {x2 = }.'
    return result


def gen_numbers_to_csv(amount: int = 128) -> None:
    """Функция, генерирующая csv файл с тремя случайными числами в каждой строке"""
    with open('source_homeworktask.csv', 'w', newline='') as f:
        for _ in range(amount):
            a = r(-42, 42)
            b = r(-42, 42)
            c = r(-42, 42)
            line = [a, b, c]
            csv_write = csv.writer(f)
            csv_write.writerow(line)


if __name__ == '__main__':
    gen_numbers_to_csv()
    square_calculation_func()