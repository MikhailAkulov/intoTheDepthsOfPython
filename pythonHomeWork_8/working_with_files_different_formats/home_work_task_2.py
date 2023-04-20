# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# * Для дочерних объектов указывайте родительскую директорию.
# * Для каждого объекта укажите файл это или директория.
# * Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

__all__ = ['directory_scan']


def directory_scan(directory: str, result_file: str) -> None:
    result_dict = []
    for dir_path, dir_name, file_name in os.walk(directory):
        if len(dir_name) != 0:
            for obj in dir_name:
                obj_dict = {'name': obj,
                            'parent_directory': dir_path.split('\\')[-1],
                            'type': 'dir',
                            'weight': _get_dir_weight(os.path.join(dir_path, obj))}
                result_dict.append(obj_dict)
        if len(file_name) != 0:
            for obj in file_name:
                obj_dict = {'name': obj,
                            'parent_directory': dir_path.split('\\')[-1],
                            'type': 'file',
                            'weight': os.path.getsize(os.path.join(dir_path, obj))}
                result_dict.append(obj_dict)
    _save_to_json(result_dict, result_file)
    _save_to_csv(result_dict, result_file)
    _save_to_pickle(result_dict, result_file)


def _get_dir_weight(dir_path: str) -> int:
    total_weight = 0
    for dir_path, _, file_names in os.walk(dir_path):
        for _ in file_names:
            fp = os.path.join(dir_path, _)

            if not os.path.islink(fp):
                total_weight += os.path.getsize(fp)
    return total_weight


def _save_to_json(data: list, file_name: str) -> None:
    with open(f'{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def _save_to_csv(data: list, file_name: str) -> None:
    with open(f'{file_name}.csv', 'w', encoding='utf-8', newline='') as f:
        csv_file = csv.DictWriter(f, fieldnames=['name', 'parent_directory', 'type', 'weight'], dialect='excel')
        csv_file.writeheader()
        csv_file.writerows(data)


def _save_to_pickle(data: list, file_name: str) -> None:
    with open(f'{file_name}.pickle', 'wb') as f:
        pickle.dump(data, f)


# if __name__ == '__main__':
#     directory_scan(os.getcwd(), 'result_home_work_task_2')
