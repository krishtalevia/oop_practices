from __future__ import annotations
import math

class Patient:

    first_name: str
    last_name: str
    surname: str
    age: int
    disease: str

    def __init__(self, first_name: str, last_name: str, surname: str, age: int, disease: str):
        self.first_name = first_name
        self.last_name = last_name
        self.surname = surname
        self.age = age
        self.disease = disease

    def make_an_appointment(self, day: int, month: str, time_hour: int, time_minutes: int):
        print(f'{self.first_name} {self.surname}, Вы записаны на прием на {day} {month}, в {time_hour}:{time_minutes}\n')

    def print_info(self):
        print(f'Имя: {self.first_name}')
        print(f'Фамилия: {self.last_name}')
        print(f'Отчество: {self.surname}')
        print(f'Возраст: {self.age}')
        print(f'Заболевание: {self.disease}')
        print()

class TouristSpot:

    name: str
    country: str
    type: str

    def __init__(self, name: str, country: str, type: str):
        self.name = name
        self.country = country
        self.type = type

    def visit(self, visiter_name: str):
        print(f'{visiter_name} посетил {self.name}, это знаменитая {self.type} достопримечательность\n')

    def print_info(self):
        print(f'Название: {self.name}')
        print(f'Страна: {self.country}')
        print(f'Тип достопримечательности: {self.type}')
        print()

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
                self.left_upper_corner_coor_x + pixels_coor_x < 0):
            print('При выполнении операции окно вышло за границы экрана по горизонтали.')
            print('Операция не была выполнена.\n')
        else:
            print(f'Операция выполнена, окно передвинулось на'
                  f' {pixels_coor_x} пикселей', 'вправо\n' if (pixels_coor_x) > 0 else 'влево\n')

        self.left_upper_corner_coor_x = self.left_upper_corner_coor_x + pixels_coor_x

    def move_by_vertical(self, pixels_coor_y: int):
        if (self.horizontal_size + (self.left_upper_corner_coor_x + pixels_coor_y) > 1080 or
                self.left_upper_corner_coor_x + pixels_coor_y < 0):
            print('При выполнении операции окно вышло за границы экрана по вертикали.')
            print('Операция не была выполнена.\n')
        else:
            print(f'Операция выполнена, окно передвинулось на'
                  f' {pixels_coor_y} пикселей', 'вверх\n' if (pixels_coor_y) > 0 else 'вниз\n')

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
        print(f'Цвет сменился с {self.color} на {color}\n')

        self.color = color

    def change_state(self, visibility: bool, border: bool):
        print('--Окно теперь имеет следующие параметры--')
        print(f'Видимость:', 'видимое' if visibility == True else 'невидимое')
        print(f'Рамка:', 'с рамкой' if border == True else 'без рамки\n')

        self.visibility = visibility
        self.border = border

    def state_status(self, visibility: bool, border: bool):
        if visibility == True:
            print(f'Состояние видимости окна:', 'видимое'
            if self.visibility == True else 'невидимое')
        if border == True:
            print(f'Состояние рамки окна:', 'с рамкой\n'
            if self.border == True else 'без рамки\n')

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
            sum += array[i]

        return sum

    @staticmethod
    def multi(array: list):
        multi = 1

        for i in range(0, len(array), 1):
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
            if max < array[i]:
                max = array[i]

        return max

    @staticmethod
    def min(array: list):
        min = array[0]

        for i in range(0, len(array), 1):
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


    def calculate_length(self):
        length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

        return length

    def __str__(self):
        return f'{self.x, self.y, self.z}'

class Fraction:

    numerator: int
    denumerator: int

    def __init__(self, numerator: int, denumerator: int):
        self.numerator = numerator
        self.denumerator = denumerator

    def __add__(self, other: Fraction):
        if self.is_denumerator_zero(other):
            return

        new_numerator = (self.numerator * other.denumerator) + (other.numerator * self.denumerator)
        new_denumerator = self.denumerator * other.denumerator

        return Fraction(new_numerator, new_denumerator)

    def __sub__(self, other: Fraction):
        if self.is_denumerator_zero(other):
            return

        new_numerator = (self.numerator * other.denumerator) - (other.numerator * self.denumerator)
        new_denumerator = self.denumerator * other.denumerator

        return Fraction(new_numerator, new_denumerator)

    def __mul__(self, other: Fraction):
        if self.is_denumerator_zero(other):
            return

        new_numerator = self.numerator * other.numerator
        new_denumerator = self.denumerator * other.denumerator

        return Fraction(new_numerator, new_denumerator)

    def is_denumerator_zero(self, other: Fraction):
        if self.denumerator == 0 or other.denumerator == 0:
            print('Знаменатель не может быть равен нулю.')
            return True
        else:
            return

    def __str__(self):
        if self.denumerator == 1:
            return f'{self.denumerator}'
        else:
            return f'{self.numerator}/{self.denumerator}'

class GeometryUtils:

    @staticmethod
    def calculate_circle_area(circle_radius: float):
        circle_area = math.pi * (circle_radius ** 2)

        return circle_area

    @staticmethod
    def calculate_circle_perimeter(circle_radius):
        circle_perimeter = (2 * math.pi) * circle_radius

        return circle_perimeter

    @staticmethod
    def calculate_rectangle_area(length: float, width: float):
        rectangle_area = length * width

        return rectangle_area

    @staticmethod
    def calculate_rectangle_perimeter(length: float, width: float):
        rectangle_perimeter = 2 * (length * width)

        return rectangle_perimeter

    @staticmethod
    def calculate_triangle_area_Heron_formula(a: float, b: float, c: float):
        semiperimeter = 0.5 * (a + b + c)

        triangle_area = (semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)) ** 0.5

        return triangle_area

class Program:

    @staticmethod
    def main():
        # Пациент
        sick = Patient('Дмитрий', 'Златопольский', 'Михайлович', 50, 'Икота')

        sick.make_an_appointment( 30, 'Июня', 12, 30)
        sick.print_info()

        # Туристическая достопримечательность
        obelisk = TouristSpot('Обелиск', 'Куба', 'историческая')

        obelisk.visit('Златопольский Дмитрий Михайлович')
        obelisk.print_info()

        # Окно
        window = ModelWindow('Окно', 100, 600, 200,
                             200, 'Белый', True, True)

        window.move_by_horizontal(100)
        window.move_by_vertical(100)
        window.change_height_width(0,100)
        window.change_color('Зеленый')
        window.change_state(False, True)
        window.state_status(True, True)
        print(window)

        # Массив
        array = [1,2,3,4]
        print('Исходный массив:', array)

        sum = ArrayUtils.sum(array)
        print('Сумма:', sum)

        multi = ArrayUtils.multi(array)
        print('Произведение:', multi)

        inversion = ArrayUtils.inversion(array)
        print('Инверсия:', inversion)

        max = ArrayUtils.max(array)
        print('Макс. элемент:', max)

        min = ArrayUtils.min(array)
        print('Мин. элемент:', min)
        print()

        # Вектор
        vector_1 = Vector(1, 2, 3)
        vector_2 = Vector(3, 2, 1)
        print('1-й вектор:', vector_1)
        print('2-й вектор:', vector_2)

        vector_3 = vector_1 + vector_2
        print('Сложение:', vector_3)

        vector_3 = vector_1 - vector_2
        print('Вычитание:',vector_3)

        vector_3 = vector_1 * vector_2
        print('Произведение:',vector_3)

        length = vector_2.calculate_length()
        print(length)

        # Дробь
        first_fraction = Fraction(6,3)
        second_fraction = Fraction(2,6)
        print('Первая дробь:', first_fraction)
        print('Вторая дробь:', second_fraction)

        third_fraction = first_fraction + second_fraction
        print('Сложение:', third_fraction)

        third_fraction = first_fraction - second_fraction
        print('Вычитание:',third_fraction)

        third_fraction = first_fraction * second_fraction
        print('Произведение:',third_fraction)

        # Геометрия
        circle_area = GeometryUtils.calculate_circle_area(3)
        print('Площадь круга:', circle_area)

        circle_perimeter = GeometryUtils.calculate_circle_perimeter(3)
        print('Периметр круга:', circle_perimeter)

        rectangle_area = GeometryUtils.calculate_rectangle_area(5, 3)
        print('Площадь прямоугольника:', rectangle_area)

        rectangle_perimeter = GeometryUtils.calculate_rectangle_perimeter(5, 3)
        print('Площадь прямоугольника:', rectangle_perimeter)

        triangle_area = GeometryUtils.calculate_triangle_area_Heron_formula(3, 3, 3)
        print('Площадь треугольника:', triangle_area)

Program.main()

