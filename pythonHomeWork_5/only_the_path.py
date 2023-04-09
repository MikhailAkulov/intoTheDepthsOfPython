# Задача:
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def path_processing(file_path: str) -> tuple[str, str, str]:
    """
    Функция обработки абсолютного пути к файлу

    :param file_path: абсолютный путь к файлу
    :return: кортеж из трёх элементов: путь, имя файла, расширение файла
    """
    *path, file_name = file_path.split('/')
    name, extension = file_name.split('.')
    path = '/'.join(path)
    return path, name, extension


file_path_local = "C:/Users/Akulo/Desktop/Geek_Brains/2_Specialization_Python/intoTheDepthsOfPython/pythonHomeWork_5/only_the_path.py"
print(path_processing(file_path_local))
file_path_web = "https://gbcdn.mrgcdn.ru/uploads/asset/4920278/attachment/0335f62338b12e3dbd73c961bffecf19.pdf"
print(path_processing(file_path_web))
