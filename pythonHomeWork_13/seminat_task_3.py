# Задание №3
# 📌 Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyBaseException(Exception):
    pass


class LevelError(MyBaseException):
    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

    def __str__(self):
        return f'Ошибка уровня: Уровень {self.value} ниже допустимого - {self.value2}'


class AccessError(MyBaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка доступа: пользователя {self.value} не существует'
