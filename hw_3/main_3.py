class Car:

    def __init__(self, brand: str, model: str, manufacture_year: int,
                 color: str, mileage: int, engine_status: bool, velocity: int):
        self.brand = brand
        self.model = model
        self.manufacture_year = manufacture_year
        self.color = color
        self.mileage = mileage
        self.engine_status = engine_status
        self.velocity = velocity

    def set_engine_status(self, status: bool):
        if not isinstance(status, bool): raise TypeError('Неправильный тип данных')

        self.engine_status = status

    def set_velocity(self, velocity: float):
        if not isinstance(velocity, float): raise TypeError('Неправильный тип данных')

        if velocity > 0 or velocity <= 200:
            self.velocity = velocity
        else:
            print('Скорость не может быть ниже нуля или выше 200 км/ч')

    def set_color(self, color: str):
        if not isinstance(color, str): raise TypeError('Неправильный тип данных')

        self.color = color

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_manufacture_year(self):
        return self.manufacture_year

    def get_color(self):
        return self.color

    def get_mileage(self):
        return self.mileage

    def get_engine_status(self):
        return self.engine_status

    def get_velocity(self):
        return self.velocity

    def __str__(self):
        return (f'Марка: {self.brand}\n'
                f'Модель: {self.model}\n'
                f'Год выпуска: {self.manufacture_year}\n'
                f'Цвет: {self.color}\n'
                f'Пробег: {self.mileage}\n'
                f'Состояние двигателя: {self.engine_status}\n'
                f'Текущая скорость: {self.velocity}\n')

class Smartphone:

    def __init__(self, brand: str, model: str, os: str, internal_memory: float,
                 ram: float, battery_charge: int, turned_on_status: bool):
        self.brand = brand
        self.model = model
        self.os = os
        self.internal_memory = internal_memory
        self.ram = ram
        self.battery_charge = battery_charge
        self.turned_on_status = turned_on_status

    def set_turned_on_status(self, status: bool):
        if not isinstance(status, bool): raise TypeError('Не подходящий тип данных')

        self.turned_on_status = status

    def set_os(self, os):
        if not isinstance(os, str): raise TypeError('Не подходящий тип данных')

        self.os = os

    def install_app(self, app_memory_volume: float):
        if not isinstance(app_memory_volume, float): raise TypeError('Не подходящий тип данных')

        if app_memory_volume > self.internal_memory: raise Exception('Недостаточно памяти')

        print('Приложение установлено')

    def delete_app(self):
        print('Приложение удалено')

    def set_battery_charge(self, battery_charge: int):
        if not isinstance(battery_charge, int): raise TypeError('Не подходящий тип данных')

        if battery_charge < 0 and battery_charge > 100: raise Exception('Не может быть меньше 0 или больше 100')

        self.battery_charge = battery_charge

    def get_turned_on_status(self):
        return self.turned_on_status

    def get_battery_charge(self):
        return self.battery_charge

    def __str__(self):
        return (f'Марка: {self.brand}\n'
                f'Модель: {self.model}\n'
                f'ОС: {self.os}\n'
                f'Объем встроенной памяти: {self.internal_memory}\n'
                f'Объем оперативной памяти: {self.ram}\n'
                f'Заряд батареи: {self.battery_charge}\n'
                f'Включен ли телефон: {self.turned_on_status}\n')

class Potion:

    def __init__(self, name: str, ingredients: list, difficulty: int, effect: str, ready_status: bool):
        self.name = name
        self.ingredients = ingredients
        self.difficulty = difficulty
        self.effect = effect
        self.ready_status = ready_status

    def add_ingredient(self, ingredient: str):
        if not isinstance(ingredient, str): raise TypeError('Не подходящий тип данных')

        self.ingredients.append(ingredient)

    def del_ingredients(self, ingredient: str):
        if not isinstance(ingredient, str): raise TypeError('Не подходящий тип данных')

        if ingredient in self.ingredients:
            for i in range(0, self.ingredients, 1):
                if self.ingredients[i] == ingredient:
                    del self.ingredients[i]
                    break

    def set_difficulty(self, difficulty: int):
        if not isinstance(difficulty, int): raise TypeError('Не подходящий тип данных')

        if difficulty < 0 and difficulty > 10: raise Exception('Не может быть меньше 0 или больше 10')

        self.difficulty = difficulty

    def set_effect(self, effect: str):
        if not isinstance(effect, str): raise TypeError('Не подходящий тип данных')

        self.effect = effect

    def get_ready_status(self):
        return self.ready_status

    def get_ingredients(self):
        return self.ingredients

    def __str__(self):
        return (f'Название: {self.name}\n'
                f'Ингредиенты: {self.ingredients}\n'
                f'Сложность приготовления: {self.difficulty}\n'
                f'Эффект зелья: {self.effect}\n'
                f'Приготовлено ли?: {self.ready_status}\n')

class Library:

    def __init__(self, name: str, adress: str, books_list: list, users_list: list):
        self.name = name
        self.adress = adress
        self.books_list = books_list
        self.users_list = users_list

    def add_book(self, book: Book):
        pass

    def remove_book(self, book: Book):
        pass

    def register_user(self, user: User):
        pass

    def issue_book(self, book: Book, user: User):
        pass

    def return_book(self, book: Book, user: User):
        pass

    @staticmethod
    def get_books_status() -> str:
        pass

    @staticmethod
    def get_users_status() -> str:
        pass

    def __str__(self):
        pass


class Book:

    def __init__(self, name: str, author: str, year: int, genre: str, in_stock: bool, current_user: User):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.in_stock = in_stock
        self.current_user = current_user

class User:

    def __str__(self, name: str, ticket_number: int, owned_books: list):
        self.name = name
        self.ticket_number = ticket_number
        self.owned_books = owned_books
