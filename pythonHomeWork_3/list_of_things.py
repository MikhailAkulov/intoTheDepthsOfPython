# Задача 4.
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things_list = {'палатка': 5, 'спальник': 2, 'продукты': 5, 'вода': 5, 'пила': 1, 'посуда': 3, 'одежда': 5}
MAX_BACKPACK_CAPACITY = 20

result_weight = 0
for thing, weight in things_list.items():
    if weight <= MAX_BACKPACK_CAPACITY:
        result_weight += weight
        print(f'{thing:<15} {weight}')
        MAX_BACKPACK_CAPACITY -= weight

print(f'Суммарный вес: {result_weight}')

