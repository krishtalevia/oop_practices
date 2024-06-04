from __future__ import annotations

# 1
class Animal:

    def __init__(self, name: str, species: str):
        self.__name = name
        self.__species = species

    def make_sound(self):
        print('Animal sound')

class Dog(Animal):

    def __init__(self, name: str, species: str):
        Animal.__init__(name, species)

    def make_sound(self):
        print('Woof')

class Cat(Animal):

    def __init__(self, name: str, species: str):
        Animal.__init__(name, species)

    def make_sound(self):
        print('Meow')

class Bird(Animal):

    def __init__(self, name: str, species: str):
        Animal.__init__(name, species)

    def make_sound(self):
        print('Chirp')

# 2
class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def introduce_yourself(self):
        print(f'Мое имя {self.__name} и мой возраст: {self.__age}.')

class Doctor(Person):

    def __init__(self, name: str, age: int):
        Person.__init__(self, name, age)

    def introduce_yourself(self):
        super().introduce_yourself()
        print('Моя профессия: врач.')


class Engineer(Person):

    def __init__(self, name: str, age: int):
        Person.__init__(self, name, age)

    def introduce_yourself(self):
        super().introduce_yourself()
        print('Моя профессия: инженер.')

class Artist(Person):

    def __init__(self, name: str, age: int):
        Person.__init__(self, name, age)

    def introduce_yourself(self):
        super().introduce_yourself()
        print('Моя профессия: художник.')

# 3
class Vehicle:  # Транспортное средство
    pass

class Automobile(Vehicle):
    pass

class Train:
    pass

class Express(Train):
    pass

# 4

class Animal:
    pass

class Mammal(Animal):
    pass

class Fish(Animal):
    pass

# class Cat(Mammal):
#     pass
#
# class Dog(Mammal):
#     pass

class Shark(Fish):
    pass

class Carp(Fish):
    pass

class Program:

    @staticmethod
    def main():

        # Зоопарк
        dog = Dog('Mel Gibson', 'Bulldog')
        dog.make_sound()

        bird = Bird('Adam Sandler', 'Pigeon')
        bird.make_sound()
        print()

        # Люди и их профессии
        doc = Doctor('Owen Wilson', 50)
        doc.introduce_yourself()
        print()


        artist = Artist('Tom Cruise', 60)
        artist.introduce_yourself()
        print()

Program.main()
