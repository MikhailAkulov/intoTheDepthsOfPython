# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
#   ✔ расширение
#   ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
#   ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
#   ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
#   ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
#   ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random


def file_generator(extension: str, min_length_name: int = 6, max_length_name: int = 30,
                   min_number_byte: int = 256, max_number_byte: int = 4096, file_count: int = 42) -> None:
    for i in range(file_count):
        string_name = ''
        random_length = random.randint(min_length_name, max_length_name)
        for j in range(random_length):
            string_name += chr(random.randint(75, 85))

        random_byte = random.randint(min_number_byte, max_number_byte)
        data = bytes(random_byte)
        with open(f'{string_name}.{extension}', 'ab') as f:
            f.write(data)


# file_generator('txt', file_count=3)
