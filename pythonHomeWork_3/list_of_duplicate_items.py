# Задача 2.
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint

source_list = [randint(1, 15) for i in range(20)]
print(f'Исходный список: {source_list}')

duplicates_list = []
result_list = []

for i in set(source_list):
    if source_list.count(i) >= 2:
        duplicates_list.append(i)
    else:
        result_list.append(i)

print(f'Список дублирующихся элементов: {duplicates_list}')
print(f'Список неповторяющихся элементов: {result_list}')
