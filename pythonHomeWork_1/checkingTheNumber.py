# Задача 2. 
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

min_limit = 0
max_limit = 100000
while True:
    print('Введите число между', min_limit, 'и', max_limit, ': ')
    num = int(input())
    if min_limit < num <= max_limit:
        break

flag = True
if num > 1:
    for i in range(2, num -1):
        if num % i == 0:
            flag = False
            break

if flag:
    message = "Введенное число является простым"
else:
    message = "Введенное число является составным"
print(message)