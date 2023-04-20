# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
from pathlib import Path

__all__ = ['add_users']

def add_users(json_file: str) -> None:
    user_ids = set()
    all_dict = {}

    if Path(json_file).exists():
        with open(json_file, 'r', encoding='utf-8') as start_file:
            all_dict = json.load(start_file)

        for _, val in all_dict.items():
            for _, id in val.items():
                user_ids.add(id)

    while True:
        name = input('Введите имя пользователя: ')
        if name == ' ':
            print('Выход из программы')
            break
        user_id = input('Введите id пользователя: ')
        if user_id in user_ids:
            print('Пользователь с таким id уже существует')
            continue
        else:
            user_ids.add(user_id)
        access_level = int(input('Введите уровень доступа от 1 до 7: '))
        if access_level < 1 or access_level > 7:
            print('Уровень доступа должен быть от 1 до 7')
            continue
        all_dict.setdefault(access_level, {})[user_id] = name

    with open(json_file, 'w', encoding='utf-8') as result_file:
        json.dump(all_dict, result_file, ensure_ascii=False, indent=2, sort_keys=True)


# if __name__ == '__main__':
#     add_users('result_task_2.json')
