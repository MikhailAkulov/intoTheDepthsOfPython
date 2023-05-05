# Задание 2.
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.

class CheckName:
    """Проверка ФИО на первую заглавную букву и наличие только букв"""
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if value and value[0] == value[0].upper() and value.isalpha():
            setattr(instance, self.param_name, value)
        elif value != '':
            raise ValueError(f'ФИО должны начинаться с заглавной буквы и содержать только буквы')

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')


class Student:
    """
    Класс Студент.
    Содержит ФИО, оценки по предметам и результаты тестов.
    Возвращает информацию об успеваемости студента.
    """
    surname = CheckName()
    name = CheckName()
    patronymic = CheckName()

    def __init__(self, surname: str, name: str, patronymic: str):
        import csv
        self.subjects = []
        self.grades = {}
        self.tests = {}
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        with open('academic_subjects.csv', 'r', newline='') as f:
            subjects = csv.reader(f, dialect='excel')
            for line in subjects:
                self.subjects.append(', '.join(line))

    def set_grade(self, subject: str, grade: int):
        """Функция для внесения оценки по предмету"""
        if subject not in self.subjects:
            print('Предмет отсутствует в перечне')
            return
        if grade < 2 or grade > 5:
            print('Оценка должна быть в диапазоне от 2 до 5')
            return
        self.grades.setdefault(subject, []).append(grade)

    def set_test_result(self, subject: str, mark: int):
        """Функция для внесения результата тестирования по предмету"""
        if subject not in self.subjects:
            print('Предмет отсутствует в перечне')
            return
        if mark < 0 or mark > 100:
            print('Результат тестирования должен быть в диапазоне от 0 до 100')
            return
        self.tests.setdefault(subject, []).append(mark)

    def __str__(self):
        import statistics
        tests = ''
        sum1 = 0
        number_of_ratings = 0
        average_grade = 0.0
        for subject, mark in self.tests.items():
            tests = f'{tests}\n{subject}: {statistics.mean(mark)}'
        for _, grade in self.grades.items():
            sum1 += sum(grade)
            number_of_ratings += len(grade)
            average_grade = sum1 / number_of_ratings
        return f'Студент: {self.surname} {self.name} {self.patronymic}\n' \
               f'{tests}\nСредний балл по предметам: {average_grade}'


if __name__ == '__main__':
    s1 = Student('Surname', 'Name', 'Patronymic')
    s1.set_grade('Mathematics', 5)
    s1.set_grade('Graphic_arts', 4)
    s1.set_grade('Sopromat', 3)
    s1.set_grade('Termech', 4)
    s1.set_grade('English', 4)
    s1.set_test_result('Mathematics', 78)
    s1.set_test_result('Mathematics', 93)
    s1.set_test_result('Graphic_arts', 82)
    s1.set_test_result('Sopromat', 73)
    s1.set_test_result('Termech', 62)
    s1.set_test_result('English', 69)
    s1.set_test_result('Termech', 81)
    s1.set_test_result('English', 89)
    s1.set_test_result('Sopromat', 84)

    print(s1)
