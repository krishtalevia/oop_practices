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

# №3
class PassengerPlane:

    def __init__(self, manufacturer: str, model: str, capacity: int, passangers: int, height: int, velocity: int):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.passangers = passangers
        self.height = height
        self.velocity = velocity

    def takeoff(self):
        if self.height > 0:
            print('Самолет уже летит.')
        else:
            print('Самолет взлетел!')
            self.height = 10

        print()

    def landing(self):
        if self.height > 0:
            print('Самолет приземлился!')
            self.height = 0
        else:
            print('Самолет находится на земле.')

        print()

    def change_height(self):
        new_height = int(input('Введите новую высоту: '))

        self.height = new_height
        print(f'Самолет теперь летит на высоте {self.height}')
        print()

    def change_velocity(self):
        new_velocity = int(input('Введите новую скорость: '))

        self.velocity = new_velocity
        print(f'Самолет теперь летит на скорости {self.velocity}')
        print()

    def print_info(self):
        print(f'Производитель: {self.manufacturer}')
        print(f'Модель: {self.model}')
        print(f'Вместимость: {self.capacity}')
        print(f'Кол-во пассажиров: {self.passangers}')
        print(f'Текущая высота: {self.height}')
        print(f'Текущая скорость: {self.velocity}')


# №4
class MusicAlbum:

    def __init__(self, performer: str, album_name: str, genre: str, track_list: list):
        self.performer = performer
        self.album_name = album_name
        self.genre = genre
        self.track_list = track_list

    def add_track(self):
        new_track_name = input('Введите название нового трека для добавления: ')

        self.track_list.append(new_track_name)
        print(f'Трек "{new_track_name}" был добавлен в альбом!')
        print()

    def delete_track(self):
        delete_track_name = input('Введите название трека для его удаления: ')

        res = f'В альбоме нет трека с названием "{delete_track_name}".'

        for i in self.track_list:
            if i == delete_track_name:
                res = f'Трек с названием "{delete_track_name}" был удален из альбома.'
                self.track_list.remove(i)

        print(res)
        print()

    def play_track(self):
        play_track_name = input('Введите название трека для его воспроизведения: ')

        res = f'В альбоме нет трека с названием "{play_track_name}".'

        for i in self.track_list:
            if i == play_track_name:
                res = f'О-о... {play_track_name}'

        print(res)
        print()

    def print_info(self):
        print(f'Исполнитель: {self.performer}')
        print(f'Название альбома: {self.album_name}')
        print(f'Жанр: {self.genre}')
        print(f'Список треков: {self.track_list}')

class Program:

    @staticmethod
    def main():
        # Животное
        betty_the_cow = Animal(name='Betty', type='Cow', age=1, sound='Moo')

        betty_the_cow.print_sound()
        betty_the_cow.print_info()

        # Книга
        random_book = Book('Интересная книга', 'И.Н. Тересный', 100)

        random_book.open_book()
        random_book.print_info()

        # Самолет
        ses_plane = PassengerPlane('Самолет Engineering School', 'M-1', 100,
                                   50, 0, 300)

        ses_plane.takeoff()
        ses_plane.landing()
        ses_plane.change_height()
        ses_plane.change_velocity()
        ses_plane.print_info()
        print()

        # Альбом
        muhozhuk = MusicAlbum('Мухожук', 'Я устал',
                              'Фолк треш-метал',
                              ['Моя оборона', 'Золотая чаша', 'От винта'])

        muhozhuk.add_track()
        muhozhuk.delete_track()
        muhozhuk.play_track()
        muhozhuk.print_info()

Program.main()


