# Задача 1:
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Задача 2:
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import choice


def get_ferz_position() -> list[list[int]]:
    """
    Функция случайной расстановки Ферзей на доске

    :return: Список координат Ферзя [строка, столбец]
    """
    ferz_positions = []
    rows = [0, 1, 2, 3, 4, 5, 6, 7]
    cols = [0, 1, 2, 3, 4, 5, 6, 7]
    while len(ferz_positions) < 8:
        x = choice(rows)
        y = choice(cols)
        ferz_positions.append([x, y])
        rows.remove(x)
        cols.remove(y)
    return ferz_positions


def show_desk(ferz_position: list[list[int]]) -> None:
    """
    Функция вывода в консоль варианта расстановки Ферзей на доске

    :param ferz_position: координаты расстановки Ферзей
    :return: None
    """
    desk = [8*["__"] for _ in range(8)]
    for ferz in ferz_position:
        desk[ferz[0]][ferz[1]] = "♕"
    for i in range(8):
        print(desk[i])


def checking_task_requirement(ferz_position: list[list[int]]) -> bool:
    """
    Функция проверки условия задачи о том чтобы Ферзи не били друг друга

    :param ferz_position: координаты расстановки Ферзей
    :return: True - Если ферзи не бьют друг друга, а если бьют - False
    """
    flag = True
    for i in range(len(ferz_position)):
        for j in range(i + 1, len(ferz_position)):
            if (ferz_position[i][0] == ferz_position[j][0] or
                    ferz_position[i][1] == ferz_position[j][1] or
                    abs(ferz_position[i][0] - ferz_position[j][0]) ==
                    abs(ferz_position[i][1] - ferz_position[j][1])):
                flag = False
                break
        if not flag:
            break
    return flag


if __name__ == "__main__":
    count = 1
    while count < 5:
        ferz = get_ferz_position()
        if checking_task_requirement(ferz):
            print(f'\nУспешная расстановка № {count}:')
            show_desk(ferz)
            print(f'Координаты Ферзей: {ferz}')
            count += 1
