# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# * doctest,
# * unittest,
# * pytest.
import unittest
import pytest


def get_conversion(number: int, mod: int = 10) -> str:
    """
    Функция получает целое число и систему исчисления, возвращает его строковое представление.
    :param number: исходное число
    :param mod: система исчисления
    :return: строковое представление
    >>> get_conversion(555, 2)
    '1000101011'
    >>> get_conversion(555, 8)
    '1053'
    >>> get_conversion(555, 16)
    '22B'
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestCaseConverter(unittest.TestCase):
    def test_2(self):
        self.assertEqual(get_conversion(555, 2), '1000101011', msg='Test failed')

    def test_8(self):
        self.assertEqual(get_conversion(555, 8), '1053', msg='Test failed')

    def test_16(self):
        self.assertEqual(get_conversion(555, 16), '22B', msg='Test failed')


def test_2():
    assert get_conversion(555, 2) == '1000101011', 'Test failed'


def test_8():
    assert get_conversion(555, 8) == '1053', 'Test failed'


def test_16():
    assert get_conversion(555, 16) == '22B', 'Test failed'


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    unittest.main()
    pytest.main()
