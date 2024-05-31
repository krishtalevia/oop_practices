from __future__ import annotations

# 1
class Car:

    def __init__(self, brand: str, model: str, year: int, price: float, status: str):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__status = status

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_status(self, status: str):
        if not isinstance(status, str): raise TypeError('Неподходящий тип данных!')

        self.__status = status

    def __str__(self):
        return (f'Бренд: {self.__brand}\n'
                f'Модель: {self.__model}\n'
                f'Год: {self.__year}\n'
                f'Цена: {self.__price}\n'
                f'Статус: {self.__status}\n')

class Saleperson:

    def __init__(self, name: str, experience: int, sold_cars: list[Car]):
        self.__name = name
        self.__experience = experience
        self.__sold_cars = sold_cars

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_year(self):
        return self.__year

    def get_sold_cars(self):
        sold_cars = '|'
        for i in self.__sold_cars:
            i = i.get_brand()
            sold_cars += f' {str(i)} |'
        return sold_cars

    def add_sold_car(self, sold_car: Car):
        if not isinstance(sold_car, Car): raise TypeError('Неподходящий тип данных!')

        self.__sold_car = sold_car

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Опыт: {self.__experience}\n'
                f'Проданные авто: {self.get_sold_cars()}\n')



