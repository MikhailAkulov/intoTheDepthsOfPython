# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv

__all__ = ['pickle_to_csv']


def pickle_to_csv(pickle_file: str, csv_file: str) -> None:
    with (
        open(pickle_file, 'rb') as pic_f,
        open(csv_file, 'w', encoding='utf-8', newline='') as csv_f
    ):
        data = pickle.load(pic_f)
        keys = []
        for key, val in data[0].items():
            keys.append(key)

        csv_file = csv.DictWriter(csv_f, fieldnames=keys, dialect='excel')
        csv_file.writeheader()
        csv_file.writerows(data)


# if __name__ == '__main__':
#     pickle_to_csv('result_task_4.pickle', 'result_task_6.csv')
