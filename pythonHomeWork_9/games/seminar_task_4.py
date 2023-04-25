# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable
from random import randint as r

__all__ = ['try_guess']


def count(param):
    def closure_func(func: Callable) -> Callable[[], None]:
        MIN_NUMBER = 1
        MAX_NUMBER = 100
        MIN_COUNT = 1
        MAX_COUNT = 10

        def wrapper(number, number_attempts, *args, **kwargs):
            for _ in range(param):
                if number < MIN_NUMBER or number > MAX_NUMBER:
                    number = r(1, 100)
                if number_attempts < MIN_COUNT or number_attempts > MAX_COUNT:
                    number_attempts = r(1, 10)
                func(number, number_attempts, *args, **kwargs)
        return wrapper
    return closure_func


@count(2)
def try_guess(number: int, number_attempts: int) -> None:
    print(f'Угадай число за {number_attempts} попыток')
    for i in range(number_attempts):
        attempt = int(input(f'Осталось попыток: {number_attempts - i}\n'))
        if attempt < number:
            print('Недобор')
        elif attempt > number:
            print('Перебор')
        else:
            print(f'Угадал с {i + 1} попытки')
            break
    else:
        print(f'Не угадал. Было загадано число: {number}')


if __name__ == '__main__':
    try_guess(100, 10)