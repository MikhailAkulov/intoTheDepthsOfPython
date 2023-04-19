# Задание №1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json

__all__ = ['txt_to_json']


def txt_to_json(txt_file: str, json_file: str) -> None:
    with(
        open(txt_file, 'r', encoding='utf-8') as f_txt,
        open(json_file, 'w', encoding='utf-8') as f_json
    ):
        my_dict = {}
        for line in f_txt:
            key, value = line.split()
            key = str(key).capitalize()
            value = float(value[:-1])
            my_dict[key] = value
        json.dump(my_dict, f_json, ensure_ascii=False, indent=4)


# if __name__ == '__main__':
#     txt_to_json('seminar_7_task_3.txt', 'result_task_1.json')

