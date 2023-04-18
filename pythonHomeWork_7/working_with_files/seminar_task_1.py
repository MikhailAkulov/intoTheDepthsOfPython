# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random

text = 'task_1.txt'
COUNT_STRING = 5
LOWER_LIMIT = -1000
UPPER_LIMIT = 1000

def file_write(count: int, name_file: str) -> None:
    with open(name_file, 'a', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{random.randint(LOWER_LIMIT, UPPER_LIMIT)} | {random.uniform(LOWER_LIMIT, UPPER_LIMIT)}\n')


# file_write(COUNT_STRING, text)
