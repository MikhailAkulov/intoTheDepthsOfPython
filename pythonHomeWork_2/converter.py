# Задача 2.
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

chars = "0123456789abcdefghijklmnopqrstuvwxyz"
MOD = 16

number = int(input("Введите целое число: "))
print(f"Проверка (ожидаемый результат) = {hex(number)}")

result = ""
if number == 0:
    result = "0"
while number != 0:
    result = chars[number % MOD] + result
    number //= MOD

print(f"Результат работы программы = 0x{result}")
