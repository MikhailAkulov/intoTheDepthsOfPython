# Задание №4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

class User:
    def __init__(self, name: str, user_id: str, access_level: int):
        self.name = name
        self.user_id = user_id
        self.access_level= access_level

    def __str__(self):
        return f'User name: {self.name}; id: {self.user_id}; access level: {self.access_level}'

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.user_id))


def user_generator(json_file_path: str) -> set[User]:
    import json
    users = set()
    with open(json_file_path, 'r') as f:
        json_file = json.load(f)
        for level in json_file:
            for key, value in json_file[level].items():
                users.add(User(value, key, level))
    return users


if __name__ == '__main__':
    print(user_generator('users.json'))