# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра
# Задание №3
# 📌 Добавьте к задачам 1 и 2 строки документации для классов.
# Задание №4
# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """
    Класс архив. При создании нового экземпляра класса, старые данные
    из ранее созданных экземпляров сохраняются в пару списков-архивов.
    """
    _count = None

    def __new__(cls, *args, **kwargs):
        if cls._count is None:
            cls._count = super().__new__(cls)
            cls._count.list_num = []
            cls._count.list_str = []
        else:
            cls._count.list_num.append(cls._count.num)
            cls._count.list_str.append(cls._count.string)
        return cls._count

    def __init__(self, num, string):
        self.num = num
        self.string = string

    def __str__(self):
        return f'Экземпляр класса Archive хранит строку {self.string} и число {self.num}.\n' \
               f'Ранее сохранено {self.list_num} и {self.list_str}'

    def __repr__(self):
        return f'Archive({self.string}, {self.num})'


if __name__ == '__main__':
    a = Archive(4, 'q')
    # print(a.list_num)
    b = Archive(3, 'y')
    c = Archive(5, 'd')
    # print(b.list_num)
    # print(b.list_str)
    # help(Archive)
    print('---------------')
    print(c)
    print('---------------')
    print(f'{c}')
    print('---------------')
    print(repr(c))
    print('---------------')
    print(f'{c = }')
