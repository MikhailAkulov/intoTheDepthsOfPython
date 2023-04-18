# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random

vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def generate_login(file_path, count: int):
    with open(file_path, 'a', encoding='utf-8') as file:
        for i in range(count):
            login = ''
            for j in range(7):
                if j == 0:
                    login += chr(random.randint(62, 85)).upper()
                elif j % 2 != 0:
                    login += chr(random.randint(62, 85)).lower()
                else:
                    login += random.choice(vowels)
            file.write(f'{login}\n')


# generate_login('task_2.txt', 10)
