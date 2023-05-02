# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)
from time import time


class MyStr(str):
    """Класс Моя Строка. Хранит имя автора и время создания."""
    def __new__(cls, autor, value):
        instance = super().__new__(cls, value)
        instance.autor = autor
        instance.time = time()
        return instance


a = MyStr("Creator", "some text")
print(a)
print(a.upper())
print(a.autor)
print(a.time)
