# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.
import json


class FileConverter:
    def __init__(self, source_file: str, result_file: str):
        self.source_file = source_file
        self.result_file = result_file
        self.convert_to_json(self.source_file, self.result_file)

    @staticmethod
    def convert_to_json(source_file: str, result_file: str) -> None:
        with(
            open(source_file, 'r', encoding='utf-8') as s_f,
            open(result_file, 'w', encoding='utf-8') as r_f
        ):
            my_dict = {}
            for line in s_f:
                key, value = line.split()
                key = str(key).capitalize()
                value = float(value[:-1])
                my_dict[key] = value
            json.dump(my_dict, r_f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    FileConverter('task_3_source.txt', 'task_3_result.json')
