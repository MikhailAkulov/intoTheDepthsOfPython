# Задание №1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from typing import Callable

__all__ = ['closure_func']


def closure_func(number: int, number_attempts: int) -> Callable[[], None]:
    def try_guess() -> bool:
        print(f'Угадай число за {number_attempts} попыток')
        for i in range(number_attempts):
            num = int(input('Введите число: '))

            if num == number:
                print('Угадал!')
                break
            elif num < number:
                print('Недобор')
            else:
                print('Перебор')
        else:
            print(f'Не угадал. Было загадано число {number}')

    return try_guess


if __name__ == '__main__':
    game = closure_func(10, 5)
    game()
