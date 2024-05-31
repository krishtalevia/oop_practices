from __future__ import annotations


# 2
class Library:

    def __init__(self, name: str, address: str, books: list[Book] = None, employees: list[Employee] = None):
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

    def add_book(self, book: Book):
        if not isinstance(book, Book): raise TypeError('Неподходящий тип данных!')

        self.__books.append(book)

    def remove_book(self, book: Book):
        if not isinstance(book, Book): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__books), 1):
            if self.__books[i] == book:
                del self.__books[i]
                break

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee): raise TypeError('Неподходящий тип данных!')

        self.__employees.append(employee)

    def remove_employee(self, employee: Employee):
        if not isinstance(employee, Employee): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__employees), 1):
            if self.__employees[i] == employee:
                del self.__employees[i]
                break

    def __str__(self):
        return (f'Название: {self.__name}'
                f'Адрес: {self.__address}'
                f'Книги: {self.get_books()}'
                f'Сотрудники: {self.get_employees()}')

class Book:

    def __init__(self, title: str, author: str, year: int, id: int, genres: list[Genre] = None):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = id
        if genres == None:
            self.__genres = []
        else:
            self.__genres = genres

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_id(self):
        return self.__id

    def get_genres(self):
        genres = '|'
        for i in self.__genres:
            i = i.get_name()
            genres += f' {str(i)} |'
        return genres

    def set_title(self, title: str):
        if not isinstance(title, str): raise TypeError('Неподходящий тип данных!')

        self.__title = title

    def set_author(self, author: str):
        if not isinstance(author, str): raise TypeError('Неподходящий тип данных!')

        self.__author = author

    def set_year(self, year: int):
        if not isinstance(year, str): raise TypeError('Неподходящий тип данных!')

        self.__year = year

    def set_id(self, id: int):
        if not isinstance(id, str): raise TypeError('Неподходящий тип данных!')

        self.__id = id

    def add_genre(self, genre: Genre):
        if not isinstance(genre, Genre): raise TypeError('Неподходящий тип данных!')

        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if not isinstance(genre, Genre): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__genres), 1):
            if self.__genres[i] == genre:
                del self.__genres[i]
                break

    def __str__(self):
        return (f'Название: {self.__title}'
                f'Автор: {self.__author}'
                f'Год: {self.__year()}'
                f'ID: {self.__id()}'
                f'Жанры: {self.get_genres()}')

class Employee:

    def __init__(self, name: str, position: str, id: int, contact_info: list[ContactInfo] = None):
        self.__name = name
        self.__position = position
        self.__id = id
        if contact_info == None:
            self.__contact_info = []
        else:
            self.__contact_info = contact_info

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        contact_info = '|'
        for i in self.__contact_info:
            i = i.get_value()
            contact_info += f' {str(i)} |'
        return contact_info

    def set_name(self, name: str):
        if not isinstance(name, str): raise TypeError('Неподходящий тип данных!')

        self.__name = name

    def set_position(self, position: str):
        if not isinstance(position, str): raise TypeError('Неподходящий тип данных!')

        self.__position = position

    def set_id(self, id: int):
        if not isinstance(id, str): raise TypeError('Неподходящий тип данных!')

        self.__id = id

    def add_contact_info(self, contact_info: ContactInfo):
        if not isinstance(contact_info, ContactInfo): raise TypeError('Неподходящий тип данных!')

        self.__contact_info.append(contact_info)

    def remove_contact_info(self, contact_info: ContactInfo):
        if not isinstance(contact_info, ContactInfo): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__contact_info), 1):
            if self.__contact_info[i] == contact_info:
                del self.__contact_info[i]
                break

    def __str__(self):
        return (f'Имя: {self.__name}'
                f'Должность: {self.__position}'
                f'ID: {self.__id()}'
                f'Контакт. информация: {self.get_contact_info()}')