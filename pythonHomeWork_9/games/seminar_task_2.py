# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.
import random
from typing import Callable

__all__ = ['deco']


def deco(func: Callable) -> Callable[[], None]:
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    MIN_COUNT = 1
    MAX_COUNT = 10

    def wrapper(number, number_attempts, *args, **kwargs):
        if not MIN_NUMBER <= number <= MAX_NUMBER:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if not MIN_COUNT <= number_attempts <= MAX_COUNT:
            number_attempts = random.randint(MIN_COUNT, MAX_COUNT)

        result = func(number, number_attempts)
    return wrapper


@deco
def guess(number, number_attempts):
    print(f'Угадай число за {number_attempts} попыток')
    for i in range(number_attempts):
        num = int(input('Введите число: '))

        if num == number:
            print(f'Угадал! число попыток: {number_attempts}')
            break
        elif num < number:
            print('Число больше')
        else:
            print('Число меньше')
    else:
        print()
        print(f'Не угадал. Было загадано число {number}, число попыток: {number_attempts}')


# guess(1000, 15)
