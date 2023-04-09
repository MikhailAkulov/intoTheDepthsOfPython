# Задача:
# Создайте функцию генератор чисел Фибоначчи

FIB_NUM = 13


def fibonacci_gen(number: int) -> (iter, int):
    """
    Функция - генератор чисел Фибоначч

    :param number: заданное значение числа Фибоначчи
    :return: лист чисел Фибоначчи от 1 до заданного значения
    """
    fibonacci_list = [0, 1, 1]
    current_number = 0
    while current_number < number:
        while len(fibonacci_list) < number:
            fibonacci_list.append(sum(fibonacci_list[-2:]))
        yield fibonacci_list[current_number]
        current_number += 1

print(f'Числа фибоначчи до {FIB_NUM}:')
for i, num in enumerate(fibonacci_gen(FIB_NUM), start=1):
    print(f'Fib {i} = {num}')
