# Задание 2.
# Создайте класс-фабрику.
# * Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# * Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Animal:

    def __init__(self, name: str = 'Nemo', age: int = None):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f'Pet name: {self.name}, age: {self.age}'


class Dog(Animal):
    def __init__(self, name: str = 'unknown', age: int = None, gender: str = '-', breed: str = '-'):
        super().__init__(name, age)
        self.gender = gender
        self.breed = breed

    def get_info(self) -> str:
        return f'Dog name: {self.name}, age: {self.age}, gender: {self.gender}, breed: {self.breed}'


class Cat(Animal):
    def __init__(self, name: str = 'unknown', age: int = None, gender: str = '-', color: str = '-'):
        super().__init__(name, age)
        self.gender = gender
        self.color = color

    def get_info(self) -> str:
        return f'Cat name: {self.name}, age: {self.age}, gender: {self.gender}, color: {self.color}'


class Hamster(Animal):
    def __init__(self, name: str = 'unknown', age: int = None, gender: str = '-', stupid: bool = False):
        super().__init__(name, age)
        self.gender = gender
        self.stupid = stupid

    def get_info(self) -> str:
        return f'Hamster name: {self.name}, age: {self.age}, gender: {self.gender}, stupid: {self.stupid}'


class Factory:
    @staticmethod
    def gen_animal(animal_type: str = '-', name: str = '-', age: int = None, gender: str = '-',
                   breed: str = '-', color: str = '-', stupid: bool = False) -> Animal:
        match (animal_type.lower()):
            case 'dog':
                return Dog(name, age, gender, breed)
            case 'cat':
                return Cat(name, age, gender, color)
            case 'hamster':
                return Hamster(name, age, gender, stupid)


if __name__ == '__main__':
    p1 = Factory.gen_animal('Dog', name='Pluto', age=8, gender='M', breed='Mops')
    p2 = Factory.gen_animal('Cat', name='Milli', age=4, gender='F', color='black')
    p3 = Factory.gen_animal('Hamster', name='Eblusha', age=1, gender='M', stupid=True)

    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())
    print(type(p1), type(p2), type(p3))
