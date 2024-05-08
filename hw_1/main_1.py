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

    def open_page(self, number_of_page: int):
        if not isinstance(number_of_page, int): raise TypeError("TypeError: number_of_page is not an int type")

        if (number_of_page > 0) and (number_of_page <= self.page_qty):
            print('Страница найдена и открыта.\n')
        else:
            print(f'Страницы с таким номером в книге нет.\n')

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
        print('Самолет взлетел!\n')

    def landing(self):
        print('Самолет приземлился!\n')


    def change_height(self, new_height: int):
        self.height = new_height
        print(f'Самолет теперь летит на высоте {self.height}\n')

    def change_velocity(self, new_velocity: int):
        self.velocity = new_velocity
        print(f'Самолет теперь летит на скорости {self.velocity}\n')

    def print_info(self):
        print(f'Производитель: {self.manufacturer}')
        print(f'Модель: {self.model}')
        print(f'Вместимость: {self.capacity}')
        print(f'Кол-во пассажиров: {self.passangers}')
        print(f'Текущая высота: {self.height}')
        print(f'Текущая скорость: {self.velocity}\n')


# №4
class MusicAlbum:

    def __init__(self, performer: str, album_name: str, genre: str, track_list: list):
        self.performer = performer
        self.album_name = album_name
        self.genre = genre
        self.track_list = track_list

    def add_track(self, new_track: str):
        self.track_list.append(new_track)
        print(f'Трек "{new_track_name}" был добавлен в альбом!\n')

    def delete_track(self, track_to_delete: str):
        res = f'В альбоме нет трека с названием "{track_to_delete}".\n'

        for i in self.track_list:
            if i == track_to_delete:
                res = f'Трек с названием "{track_to_delete}" был удален из альбома.\n'
                self.track_list.remove(i)

        print(res)
        print()

    def play_track(self, track_to_play: str):
        res = f'В альбоме нет трека с названием "{track_to_play}".\n'

        for i in self.track_list:
            if i == track_to_play:
                res = f'О-о... {track_to_play}'

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

        random_book.open_page(number_of_page=99)
        random_book.print_info()

        # Самолет
        ses_plane = PassengerPlane('Самолет Engineering School', 'M-1', 100,
                                   50, 0, 300)

        ses_plane.takeoff()
        ses_plane.landing()
        ses_plane.change_height(new_height=10)
        ses_plane.change_velocity(new_velocity=10)
        ses_plane.print_info()
        print()

        # Альбом
        muhozhuk = MusicAlbum('Мухожук', 'Я устал',
                              'Фолк треш-метал',
                              ['Моя оборона', 'Золотая чаша', 'От винта'])

        muhozhuk.add_track(new_track='Новый')
        muhozhuk.delete_track(track_to_delete='Золотая чаша')
        muhozhuk.play_track(track_to_play='От винта')
        muhozhuk.print_info()

Program.main()


