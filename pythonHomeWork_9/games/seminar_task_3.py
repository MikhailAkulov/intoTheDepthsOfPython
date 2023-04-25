# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат,
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.
import json
from typing import Callable, Any


def log_to_json(func: Callable) -> Callable:
    json_file = f'{func.__name__}.json'
    data = []
    with open(json_file, mode='r', encoding="utf-8") as f_r:
        data = json.load(f_r)
    def wrapper(*args, **kwargs) -> Any:
        result = func(args, kwargs)
        json_file = f'{func.__name__}.json'
        json_dict = {'args': args, **kwargs, 'res': result}
        data.append(json_dict)
        with open(json_file, mode='w', encoding="utf-8") as f:
            json.dump(data, f)

        return result

    return wrapper

@log_to_json
def show(*args, **kwargs):
    print(*args, **kwargs)

if __name__ == '__main__':
    show(1, 3, k=4)