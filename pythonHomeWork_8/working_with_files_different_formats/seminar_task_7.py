# Задание №7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.

import csv
import pickle

__all__ = ['csv_to_pickle_str']


def csv_to_pickle_str(csv_file: str) -> None:
    with open(csv_file, 'r', newline='') as csv_f:
        csv_file = csv.reader(csv_f, dialect='excel')

        data = []
        for line in csv_file:
            data.append(line)

        result = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(result)


# if __name__ == '__main__':
#     csv_to_pickle_str('result_task_6.csv')
