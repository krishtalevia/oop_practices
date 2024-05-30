from __future__ import annotations


# 2
class Library:

    def __init__(self, name: str, address: str, books: list[Book], employees: list[Employee]):
        self.__name = name
        self.__address = address
        if books is None:
            self.__books = []
        else:
            self.__books = books
        if employees is None:
            self.__employees = []
        else:
            self.__employees = employees

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_books(self):
        books = '|'
        for i in self.__books:
            i = i.get_title()
            books += f' {str(i)} |'
        return books

    def get_employees(self):
        employees = '|'
        for i in self.__books:
            i = i.get_name()
            employees += f' {str(i)} |'
        return employees

    def set_name(self, name: str):
        if not isinstance(name, str): raise TypeError('Неподходящий тип данных!')

        self.__name = name

    def set_address(self, address: str):
        if not isinstance(address, str): raise TypeError('Неподходящий тип данных!')

        self.__address = address

    def __str__(self):
        return (f'Название: {self.__name}'
                f'Адрес: {self.__address}'
                f'Книги: {self.get_books()}'
                f'Сотрудники: {self.get_employees()}')

