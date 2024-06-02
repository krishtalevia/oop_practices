from __future__ import annotations

# 1
class Animal:

    def __init__(self, name: str, species: str):
        self.__name = name
        self.__species = species

    def make_sound(self):
        print('Animal sound')

class Dog(Animal):

    def make_sound(self):
        print('Woof')

class Cat(Animal):

    def make_sound(self):
        print('Meow')

class Bird(Animal):

    def make_sound(self):
        print('Chirp')

# 2
class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def introduce_yourself(self):
        print(f'Мое имя {self.__name} и мой возраст: {self.__age}.')

class Program:

    @staticmethod
    def main():

        dog = Dog('Mel Gibson', 'Bulldog')
        dog.make_sound()
        bird = Bird('Adam Sandler', 'Pigeon')
        bird.make_sound()

Program.main()
