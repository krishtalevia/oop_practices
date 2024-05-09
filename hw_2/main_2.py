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
    visible: bool
    border: bool

    def __init__(self, title: str, left_upper_corner_coor_x: int, left_upper_corner_coor_y: int,
                 horizontal_size: int, vertical_size: int, color: str, visible: bool, border: bool):
        pass

# window = ModelWindow('window', 1000, 500, 500,
#                      500, 'white', True, True)

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


    def change_height_width(self):
        pass

    def change_color(self, color: str):
        print(f'Цвет сменился с {self.color} на {color}')

        self.color = color

    def change_state(self):
        pass

    def window_state_status(self):
        pass

    def __str__(self):
        pass
