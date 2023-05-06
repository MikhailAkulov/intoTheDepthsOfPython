# Задание №2
# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.

def get_value(dict_: {}, key: str, default_value=None):
    try:
        value = dict_[key]
    except KeyError:
        value = default_value
    return value


if __name__ == '__main__':
    my_dict = {'one': 1, 'two': 2, 'three': 3}
    print(get_value(my_dict, 'four'))
