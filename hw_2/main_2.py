from __future__ import annotations

class Patient:

    full_name: str
    age: int
    disease: str

    def __init__(self, full_name: str, age: int, disease: str):
        self.full_name = full_name
        self.age = age
        self.disease = disease

    def make_an_appointment(self, day: int, month: str, time_hour: int, time_minutes: int):
        print(f'{self.full_name}, Вы записаны на прием на {day} {month}, в {time_hour}:{time_minutes}')

    def print_info(self):
        print(f'ФИО: {self.full_name}')
        print(f'Возраст: {self.age}')
        print(f'Заболевание: {self.full_name}')

class TouristSpot:

    name: str
    country: str
    type: str

    def __init__(self, name: str, country: str, type: str):
        self.name = name
        self.country = country
        self.type = type

    def visit(self, visiter_name: str):
        print(f'{visiter_name} посетил {self.name}, знаменитая {self.type} достопримечательность')

    def print_info(self):
        print(f'Название: {self.name}')
        print(f'Страна: {self.country}')
        print(f'Тип достопримечательности: {self.type}')

class ModelWindow:

    title: str
    left_upper_corner_coor_x: int
    left_upper_corner_coor_y: int
    horizontal_size: int
    vertical_size: int
    color: str
    visibility: bool
    border: bool

    def __init__(self, title: str, left_upper_corner_coor_x: int, left_upper_corner_coor_y: int,
                 horizontal_size: int, vertical_size: int, color: str, visibility: bool, border: bool):
        self.title = title
        self.left_upper_corner_coor_x = left_upper_corner_coor_x
        self.left_upper_corner_coor_y = left_upper_corner_coor_y
        self.horizontal_size = horizontal_size
        self.vertical_size = vertical_size
        self.color = color
        self.visibility = visibility
        self.border = border

    def move_by_horizontal(self, pixels_coor_x: int):
        if (self.horizontal_size + (self.left_upper_corner_coor_x + pixels_coor_x) > 1960 or
                self.horizontal_size + (self.left_upper_corner_coor_x + pixels_coor_x) < 0):
            print('При выполнении операции окно вышло за границы экрана по горизонтали.')
            print('Операция не была выполнена.\n')
        else:
            print(f'Операция выполнена, окно передвинулось на'
                  f'{pixels_coor_x} пикселей', 'вправо\n' if (pixels_coor_x) > 0 else 'влево\n')

        self.left_upper_corner_coor_x = self.left_upper_corner_coor_x + pixels_coor_x

    def move_by_vertical(self, pixels_coor_y: int):
        if (self.horizontal_size + (self.left_upper_corner_coor_x + pixels_coor_y) > 1080 or
                self.horizontal_size + (self.left_upper_corner_coor_x + pixels_coor_y) < 0):
            print('При выполнении операции окно вышло за границы экрана по вертикали.')
            print('Операция не была выполнена.\n')
        else:
            print(f'Операция выполнена, окно передвинулось на'
                  f'{pixels_coor_y} пикселей', 'вверх\n' if (pixels_coor_y) > 0 else 'вниз\n')

        self.left_upper_corner_coor_y = self.left_upper_corner_coor_y + pixels_coor_y

    def change_height_width(self, height = 0, width = 0):
        if height != 0:
            if ((height + self.vertical_size) + self.left_upper_corner_coor_y > 1080 or
                (height + self.vertical_size) + self.left_upper_corner_coor_y < 0):
                print('При выполнении операции окно вышло за границы экрана по высоте.')
                print('Операция не была выполнена.\n')
            else:
                print('Окно', 'увеличено' if height > 0 else 'уменьшено', f'на {height}\n')

                self.vertical_size = self.vertical_size + height

        if width != 0:
            if ((width + self.horizontal_size) + self.left_upper_corner_coor_x > 1960 or
                    (width + self.horizontal_size) + self.left_upper_corner_coor_x < 0):
                print('При выполнении операции окно вышло за границы экрана по широте.')
                print('Операция не была выполнена.\n')
            else:
                print('Окно', 'увеличено' if width > 0 else 'уменьшено', f'на {width}\n')

                self.horizontal_size = self.horizontal_size + width

    def change_color(self, color: str):
        print(f'Цвет сменился с {self.color} на {color}')

        self.color = color

    def change_state(self, visibility: bool, border: bool):
        print('--Окно теперь имеет следующие параметры--')
        print(f'Видимость:', 'видимое' if visibility == True else 'невидимое')
        print(f'Рамка:', 'с рамкой' if border == True else 'без рамки')

        self.visibility = visibility
        self.border = border

    def state_status(self, visibility: bool, border: bool):
        if visibility == True:
            print(f'Состояние видимости окна:', 'видимое'
            if self.visibility == True else 'невидимое')
        if border == True:
            print(f'Состояние рамки окна:', 'с рамкой'
            if self.border == True else 'без рамки')

    def __str__(self):
        return (f'Заголовок: {self.title}\n'
                f'Координата левого верхнего угла x: {self.left_upper_corner_coor_x}\n'
                f'Координата левого верхнего угла y: {self.left_upper_corner_coor_y}\n'
                f'Размер по горизонтали: {self.horizontal_size}\n'
                f'Размер по вертикали: {self.vertical_size}\n'
                f'Цвет: {self.color}\n'
                f'Видимость: {'видимое' if self.visibility == True else 'невидимое'}\n'
                f'Окно: {'с рамкой' if self.border == True else 'без рамки'}\n')

class ArrayUtils:

    @staticmethod
    def sum(array: list):
        sum = 0

        for i in range(0, len(array), 1):
            if array[i].isdigit():
                sum += array[i]

        return sum

    @staticmethod
    def multi(array: list):
        multi = 1

        for i in range(0, len(array), 1):
            if array[i].isdigit():
                multi *= array[i]

        return multi

    @staticmethod
    def inversion(array: list):
        inversed_array = []
        for i in range(len(array) -1, -1, -1):
            inversed_array.append(array[i])

        return inversed_array

    @staticmethod
    def max(array: list):
        max = array[0]

        for i in range(0, len(array), 1):
            if array[i].isdigit():
                if max < array[i]:
                    max = array[i]

        return max

    @staticmethod
    def min(array: list):
        min = array[0]

        for i in range(0, len(array), 1):
            if array[i].isdigit():
                if min > array[i]:
                    min = array[i]

        return min

class Vector:

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: Vector):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z

        return Vector(new_x, new_y, new_z)

    def __sub__(self, other: Vector):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z

        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            new_z = self.z * other.z

            return Vector(new_x, new_y, new_z)
        else:
            new_x = self.x * other
            new_y = self.y * other
            new_z = self.z * other

            return Vector(new_x, new_y, new_z)


    def length_calculation(self):
        length = (self.x ** 2, self.y ** 2, self.z ** 2) ** 0.5

        return length

    def __str__(self):
        return f'({self.x, self.y, self.z})'