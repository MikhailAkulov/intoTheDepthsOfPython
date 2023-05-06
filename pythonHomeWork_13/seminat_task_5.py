# Задание №5
# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя.
# Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа.
# А если пользователь есть, получите его уровень из множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
from seminat_task_3 import AccessError, LevelError
from seminat_task_4 import User


class TestProject:
    users_set = set()
    TEST_LEVEL = 7

    def user_generator(self, json_file_path: str) -> set[User]:
        import json
        with open(json_file_path, 'r') as f:
            json_file = json.load(f)
            for level in json_file:
                for key, value in json_file[level].items():
                    self.users_set.add(User(value, key, level))
        return self.users_set

    def enter(self, user_name, user_id) -> User:
        for user in self.users_set:
            if User(user_name, user_id, 0) == user:
                user_access_level = user.access_level
                return User(user_name, user_id, user_access_level)
        raise AccessError(user_name)

    def add_user(self, name, user_id, access_level) -> User:
        if access_level >= self.TEST_LEVEL:
            u1 = User(name, user_id, access_level)
            self.users_set.add(u1)
            return u1
        raise LevelError(access_level, self.TEST_LEVEL)
