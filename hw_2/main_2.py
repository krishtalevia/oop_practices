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
    left_upper_corner_coor: int
    horizontal_size: int
    vertical_size: int
    color: str
    visible: bool
    border: bool

    def __init__(self, title: str, left_upper_corner_coor: int, horizontal_size: int,
                 vertical_size: int, color: str, visible: bool, border: bool):
        pass

    def moving_by_horizontal(self):
        pass

    def moving_by_vertical(self):
        pass

    def change_height_width(self):
        pass

    def change_color(self):
        pass

    def change_state(self):
        pass

    def window_state_status(self):
        pass

    def __str__(self):
        pass
