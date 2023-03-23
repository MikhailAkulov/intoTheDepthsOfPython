# Задача 3.
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions
import math

fraction1 = input('Введите первую дробь: ').split('/')
fraction2 = input('Введите вторую дробь: ').split('/')
print('===============================')

numerator1 = int(fraction1[0])
denominator1 = int(fraction1[1])
numerator2 = int(fraction2[0])
denominator2 = int(fraction2[1])

numerator_sum = numerator1 * denominator2 + numerator2 * denominator1
denominator_sum = denominator1 * denominator2

gcd_for_sum = math.gcd(numerator_sum, denominator_sum)
if gcd_for_sum:
    numerator_sum //= gcd_for_sum
    denominator_sum //= gcd_for_sum

numerator_multi = numerator1 * numerator2
denominator_multi = denominator1 * denominator2

gcd_for_multi = math.gcd(numerator_multi, denominator_multi)
if gcd_for_multi:
    numerator_multi //= gcd_for_multi
    denominator_multi //= gcd_for_multi

print(f'Сумма дробей по программе: {numerator_sum}/{denominator_sum}')
print(f'Сумма по модулю fractions: {fractions.Fraction(numerator1, denominator1) + fractions.Fraction(numerator2, denominator2)}')
print('===============================')
print(f'Произведение дробей по программе: {numerator_multi}/{denominator_multi}')
print(f'Произведение по модулю fractions: {fractions.Fraction(numerator1, denominator1) * fractions.Fraction(numerator2, denominator2)}')