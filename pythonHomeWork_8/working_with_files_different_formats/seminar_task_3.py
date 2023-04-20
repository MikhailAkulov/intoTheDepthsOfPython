# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import json
import csv

__all__ = ['json_to_csv']

def json_to_csv(json_file: str) -> None:
    with open(json_file, 'r', encoding='utf-8') as source_f:
        users_dict = json.load(source_f)

    users_data = [[lvl, u_id, u_name]
                  for lvl, usr in users_dict.items()
                  for u_id, u_name in usr.items()]
    csv_file = f'{json_file.split(".")[0]}.csv'
    with open(csv_file, 'w', encoding='utf-8') as result_f:
        csv_writer = csv.writer(result_f, dialect='excel')
        csv_writer.writerows(users_data)


# if __name__ == '__main__':
#     json_to_csv('result_task_2.json')
