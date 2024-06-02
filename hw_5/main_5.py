from __future__ import annotations

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

class Program:

    @staticmethod
    def main():

        dog = Dog('Mel Gibson', 'Bulldog')
        dog.make_sound()
        bird = Bird('Adam Sandler', 'Pigeon')
        bird.make_sound()

Program.main()