# Задание №7 (из семинара)
# 📌 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# 📌 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# 📌 Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# 📌 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# 📌 Проверку года на високосность вынести в отдельную защищённую функцию.

# Д/З. Задание №2:
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

__all__ = ['checking_for_existence']


def checking_for_existence(input_date: str) -> bool:
    """
    Функция провеерки возможности существования даты

    :param input_date: дата
    :return: True или False
    """
    numbers = list(map(int, input_date.split('.')))
    day, month, year = numbers
    if 1 <= year <= 9999 or 1 <= month <= 12 or 1 <= day <= 31:
        match month:
            case 4 | 6 | 9 | 11:
                if day == 31:
                    return False
                else:
                    return True
            case 2:
                if day == 29 and not _checking_for_a_leap_year(year) or day > 29:
                    return False
                else:
                    return True
            case _:
                return True
    return False


def _checking_for_a_leap_year(year: int) -> bool:
    """
    Защищенная функция проверки даты на високосный год

    :param year: год из указанной даты
    :return: True или False
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


test_data_1 = "01.01.0001"
test_data_2 = "31.12.9999"
test_data_3 = "29.02.1988"
test_data_4 = "29.02.2023"
test_data_5 = "13.04.2023"

if __name__ == '__main__':
    """Для запуска из файла"""
    # print(f'Дата {test_data_1}: {checking_for_existence(test_data_1)}')
    # print(f'Дата {test_data_2}: {checking_for_existence(test_data_2)}')
    # print(f'Дата {test_data_3}: {checking_for_existence(test_data_3)}')
    # print(f'Дата {test_data_4}: {checking_for_existence(test_data_4)}')
    # print(f'Дата {test_data_5}: {checking_for_existence(test_data_5)}')

    """Для запуска из терминала с вводом даты в формате DD.MM.YYYY"""
    name, arg = argv
    print(checking_for_existence(arg))
