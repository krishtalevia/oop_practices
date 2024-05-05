# №1

class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name
        self.type = type
        self.age = age
        self.sound = sound

    def print_sound(self):
        print(f'{self.name} издает звук "{self.sound}"')

    def print_info(self):
        print(f'Имя: {self.name}')
        print(f'Вид: {self.type}')
        print(f'Возраст: {self.age}')
        print(f'Издаваемый звук: {self.sound}')
        