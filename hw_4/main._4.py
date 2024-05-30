from __future__ import annotations


# 1
class Student:

    def __init__(self, first_name: str, last_name: str, age: int, avg_mark: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__avg_mark = avg_mark

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_avg_mark(self):
        return self.__avg_mark

    def set_first_name(self, first_name: str):
        if not isinstance(first_name, str): raise TypeError('Неподходящий тип данных!')

        self.__first_name = first_name

    def set_last_name(self, last_name: str):
        if not isinstance(last_name, str): raise TypeError('Неподходящий тип данных!')

        self.__last_name = last_name

    def set_age(self, age: int):
        if not isinstance(age, int): raise TypeError('Неподходящий тип данных!')

        self.__age = age

    def set_avg_mark(self, avg_mark: int):
        if not isinstance(avg_mark, int): raise TypeError('Неподходящий тип данных!')

        self.__avg_mark = avg_mark

    def __str__(self):
        return (f'Имя: {self.__first_name}'
                f'Фамилия: {self.__last_name}'
                f'Возраст: {self.__age}'
                f'Средний балл: {self.__avg_mark}')

    def __eq__(self, other):
        if not isinstance(other, Student): raise TypeError('Неподходящий тип данных!')

        if self.__avg_mark == other.__avg_mark:
            return True

        return False

    def __ne__(self, other):
        if not isinstance(other, Student): raise TypeError('Неподходящий тип данных!')

        if self.__avg_mark != other.__avg_mark:
            return True

        return False

    def __lt__(self, other):
        if not isinstance(other, Student): raise TypeError('Неподходящий тип данных!')

        if self.__avg_mark < other.__avg_mark:
            return True

        return False

    def __le__(self, other):
        if not isinstance(other, Student): raise TypeError('Неподходящий тип данных!')

        if self.__avg_mark <= other.__avg_mark:
            return True

        return False

    def __gt__(self, other):
        if not isinstance(other, Student): raise TypeError('Неподходящий тип данных!')

        if self.__avg_mark > other.__avg_mark:
            return True

        return False

    def __ge__(self, other):
        if not isinstance(other, Student): raise TypeError('Неподходящий тип данных!')

        if self.__avg_mark >= other.__avg_mark:
            return True

        return False

class Program:

    @staticmethod
    def main():

        ivan_the_student = Student('Иван', 'Иванов', 30, 4)
        oleg_the_student = Student('Олег', 'Олегов', 26, 5)

        print(ivan_the_student < oleg_the_student)
        print(ivan_the_student == oleg_the_student)

Program.main()