# №1
class Animal:

    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name
        self.type = type
        self.age = age
        self.sound = f'"{sound}"'

    def print_sound(self):
        print(f'{self.name} издает звук {self.sound}')
        print()

    def print_info(self):
        print(f'Имя: {self.name}')
        print(f'Вид: {self.type}')
        print(f'Возраст: {self.age}')
        print(f'Издаваемый звук: {self.sound}')
        print()


class Program:

    @staticmethod
    def main():
        betty_the_cow = Animal(name='Betty', type='Cow', age=1, sound='Moo')

        betty_the_cow.print_sound()
        betty_the_cow.print_info()

Program.main()

# №2
class Book:

    def __init__(self, name: str, author: str, page_qty: int):
        self.name = name
        self.author = author
        self.page_qty = page_qty

    def open_book(self):
        page_num = int(input('Введите номер страницы: '))

        if page_num > self.page_qty or page_num < 0:
            print(f'Страницы с таким номером в книге нет.')
        else:
            print(f'Страница открылась.')

        print()

    def print_info(self):
        print(f'Название книги: {self.name}')
        print(f'Автор: {self.author}')
        print(f'Кол-во страниц: {self.page_qty}')
        print()

class Program:

    @staticmethod
    def main():
        random_book = Book('Интересная книга', 'И.Н. Тересный', 100)

        random_book.open_book()
        random_book.print_info()

Program.main()

# №3
class PassengerPlane:

    def __init__(self, manufacturer: str, model: str, capacity: int, passangeres: int, height: int, velocity: int):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.passangers = passangeres
        self.height = height
        self.velocity = velocity

