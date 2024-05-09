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
