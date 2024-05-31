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

    def set_price(self, price: float):
        if not isinstance(price, float): raise TypeError('Неподходящий тип данных!')

        self.__price = price

    def __str__(self):
        return (f'Бренд: {self.__brand}\n'
                f'Модель: {self.__model}\n'
                f'Год: {self.__year}\n'
                f'Цена: {self.__price}\n'
                f'Статус: {self.__status}\n')


class Salesperson:

    def __init__(self, name: str, experience: int, sold_cars: list[Car]):
        self.__name = name
        self.__experience = experience
        self.__sold_cars = sold_cars

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_sold_cars(self):
        sold_cars = '|'
        for i in self.__sold_cars:
            i = i.get_brand()
            sold_cars += f' {str(i)} |'
        return sold_cars

    def add_sold_car(self, sold_car: Car):
        if not isinstance(sold_car, Car): raise TypeError('Неподходящий тип данных!')

        self.__sold_cars.append(sold_car)

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Опыт: {self.__experience}\n'
                f'Проданные авто: {self.get_sold_cars()}\n')


class Customer:

    def __init__(self, name: str, phone_num: int, email: str, cars: list[Car]):
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__cars = cars

    def get_name(self):
        return self.__name

    def get_phone_num(self):
        return self.__phone_num

    def get_email(self):
        return self.__email

    def get_cars(self):
        cars = '|'
        for i in self.__cars:
            i = i.get_brand()
            cars += f' {str(i)} |'
        return cars

    def add_car(self, car: Car):
        if not isinstance(car, Car): raise TypeError('Неподходящий тип данных!')

        self.__cars.append(car)

    def remove_car(self, car: Car):
        if not isinstance(car, Car): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__cars), 1):
            if self.__cars[i] == car:
                del self.__cars[i]
                break

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Номер тел.: {self.__phone_num}\n'
                f'Эл. почта: {self.__email}\n'
                f'Список авто: {self.get_cars()}\n')

class Dealership:

    def __init__(self, cars: list[Car], salespersons: list[Salesperson], customers: list[Customer]):
        self.__cars = cars
        self.__salespersons = salespersons
        self.__customers = customers

    def get_cars(self):
        cars = '|'
        for i in self.__cars:
            i = i.get_brand()
            cars += f' {str(i)} |'
        return cars

    def get_salespersons(self):
        salespersons = '|'
        for i in self.__salespersons:
            i = i.get_name()
            salespersons += f' {str(i)} |'
        return salespersons

    def get_customers(self):
        customers = '|'
        for i in self.__customers:
            i = i.get_name()
            customers += f' {str(i)} |'
        return customers

    def add_car(self, car: Car):
        if not isinstance(car, Car): raise TypeError('Неподходящий тип данных!')

        self.__cars.append(car)

    def remove_car(self, car: Car):
        if not isinstance(car, Car): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__cars), 1):
            if self.__cars[i] == car:
                del self.__cars[i]
                break

    def sell_car(self, car: Car, salesperson: Salesperson, customer: Customer):
        if not isinstance(car, Car) \
                or not isinstance(salesperson, Salesperson) \
                or not isinstance(customer, Customer): raise TypeError('Неподходящий тип данных!')

        if car in self.__cars:
            car.set_status('Продано')
            salesperson.add_sold_car(car)
            customer.add_car(car)

            self.remove_car(car)

    def add_salesperson(self, salesperson: Salesperson):
        if not isinstance(salesperson, Salesperson): raise TypeError('Неподходящий тип данных!')

        self.__salespersons.append(salesperson)

    def remove_salesperson(self, salesperson: Salesperson):
        if not isinstance(salesperson, Salesperson): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__salespersons), 1):
            if self.__salespersons[i] == salesperson:
                del self.__salespersons[i]
                break

    def add_customer(self, customer: Customer):
        if not isinstance(customer, Customer): raise TypeError('Неподходящий тип данных!')

        self.__customers.append(customer)

    def set_car_price(self, car: Car, price: float):
        if not isinstance(car, Car) \
                or not isinstance(price, float): raise TypeError('Неподходящий тип данных!')

        if not price > 0: raise ValueError('Цена не может быть меньше 0')

        car.set_price(price)

    def __str__(self):
        return (f'Авто: {self.get_cars()}\n'
                f'Продавцы: {self.get_salespersons()}\n'
                f'Клиенты: {self.get_customers()}\n')

class Program:

    @staticmethod
    def main():
        first_car = Car('ВАЗ', '01', 1400, 1000, 'Продано')
        second_car = Car('АВЗ', '02', 1401, 2000, 'В наличии')
        third_car = Car('ЗАВ', '03', 1402, 3000, 'Ожидается')

        oleg_the_salesperson = Salesperson('Олег', 2, [first_car])

        igor_the_customer = Customer('Игорь', 89123456789, 'igor@email.com', [first_car])

        first_dealership = Dealership([second_car, third_car], [oleg_the_salesperson],
                                      [igor_the_customer])

        # print(first_car)
        # print(oleg_the_salesperson)
        # print(first_dealership)
        #
        # first_dealership.sell_car(third_car, oleg_the_salesperson, igor_the_customer)
        #
        # print(igor_the_customer)
        #
        # print(first_dealership)

        first_dealership.set_car_price(first_car, 5000.00)
        print(first_car)


Program.main()
