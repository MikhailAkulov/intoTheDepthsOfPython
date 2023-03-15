# Задача 3. 
# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUMBER_OF_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print('Попробуйте угадать число от', LOWER_LIMIT, 'до', UPPER_LIMIT)
for i in range(NUMBER_OF_ATTEMPTS):
    enter = int(input('Доступно попыток - {}. Введите число: '.format(NUMBER_OF_ATTEMPTS - i)))
    if enter == num:
        print('Поздравляю, число угадано!')
        break
    elif num > enter:
        message = 'Загаданное число больше'
    else:
        message = 'Загаданное число меньше'
    print(message)
else:
    print('Попытки закончились, повезёт в другой раз')
