from __future__ import annotations

# 1.1
class Wizard:

    def __init__(self, name: str, house: str, magic_level: int, spells: list, status: str):
        self.__name = name
        self.__house = house
        self.__magic_level = magic_level
        if spells == None:
            self.__spells = []
        else:
            self.__spells = spells
        self.__status = status

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_magic_level(self):
        return self.__magic_level

    def get_spells(self):
        return self.__spells

    def get_status(self):
        return self.__status

    def set_house(self, house: str):
        if not isinstance(house, str): raise('Не подходящий тип данных.')

        self.__house = house

    def set_magic_level(self, magic_level: int):
        if not isinstance(magic_level, int): raise('Не подходящий тип данных.')

        if magic_level > 0:
            self.__magic_level = magic_level

    def set_status(self, status: str):
        if not isinstance(status, str): raise('Не подходящий тип данных.')

        self.__status = status

    def add_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise('Не подходящий тип данных.')

        self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise('Не подходящий тип данных.')

        for i in range(0, len(self.__spells), 1):
            if self.__spells[i] == spell:
                del self.__spells[i]
                break

    def increase_magic_level(self, amount: int):
        if not isinstance(amount, int): raise('Не подходящий тип данных.')

        if amount > 0:
            self.__magic_level += amount

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Факультет: {self.__house}\n'
                f'Уровень маг. силы: {self.__magic_level}\n'
                f'Список заклинаний: {self.__spells}\n'
                f'Статус: {self.__status}')

# 1.2
class Spell:

    def __init__(self, name: str, level: int, type: str, description: str):
        self.__name = name
        self.__level = level
        self.__type = type
        self.__description = description

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

    def set_name(self, name: str):
        if not isinstance(name, str): raise('Не подходящий тип данных.')

        self.__name = name

    def set_level(self, level: int):
        if not isinstance(level, int): raise('Не подходящий тип данных.')

        if level <= 10 and level >= 0:
            self.__level = level

    def set_type(self, type: str):
        if not isinstance(type, str): raise('Не подходящий тип данных.')

        self.__type = type

    def set_description(self, description: str):
        if not isinstance(description, str): raise('Не подходящий тип данных.')

        self.__description = description

    def __str__(self):
        return (f'Название: {self.__name}\n'
                f'Уровень сложности: {self.__level}\n'
                f'Тип заклинания: {self.__type}\n'
                f'Описание: {self.__description}\n')

# 2

class Employee:

    def __init__(self, name: str, position: str, department: str, salary: float, experience: int, projects: list):
        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__experience = experience
        if projects == None:
            self.__projects = []
        else:
            self.__projects = projects

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_department(self):
        return self.__department

    def get_salary(self):
        return self.__salary

    def get_experience(self):
        return self.__experience

    def get_projects(self):
        return self.__projects

    def set_name(self, name: str):
        if not isinstance(name, str): raise('Не подходящий тип данных.')

        self.__name = name

    def set_position(self, position: str):
        if not isinstance(position, str): raise('Не подходящий тип данных.')

        self.__position = position

    def set_department(self, department: str):
        if not isinstance(department, str): raise('Не подходящий тип данных.')

        self.__department = department

    def set_salary(self, salary: float):
        if not isinstance(salary, float): raise('Не подходящий тип данных.')

        self.__salary = salary

    def set_experience(self, experience: int):
        if not isinstance(experience, int): raise('Не подходящий тип данных.')

        self.__experience = experience

    def add_project(self, project: str):
        if not isinstance(project, str): raise('Не подходящий тип данных.')

        self.__projects.append(project)

    def remove_project(self, project: str):
        if not isinstance(project, str): raise('Не подходящий тип данных.')

        for i in range(0, len(self.__projects), 1):
            if self.__projects[i] == project:
                del self.__projects[i]
                break

    def increase_salary(self, salary: float):
        if not isinstance(salary, float): raise('Не подходящий тип данных.')

        if salary > 0:
            self.__salary += salary

    def __str__(self):
        return (f'Название: {self.__name}\n'
                f'Должность: {self.__position}\n'
                f'Отдел: {self.__department}\n'
                f'Зарплата: {self.__salary}\n'
                f'Опыт: {self.__experience}\n'
                f'Проекты: {self.__projects}')

class Robot:

    def __init__(self, serial_num: int, model: str, task: str, battery: int, status: bool):
         self.__serial_num = serial_num
         self.__model = model
         self.__task = task
         self.__battery = battery
         self.__status = status

    def get_serial_num(self):
        return self.__serial_num

    def get_model(self):
        return self.__model

    def get_task(self):
        return self.__task

    def get_battery(self):
        return self.__battery

    def get_status(self):
        return self.__status

    def set_serial_num(self, serial_num: int):
        if not isinstance(serial_num, int): raise('Не подходящий тип данных.')

        self.__serial_num = serial_num

    def set_model(self, model: str):
        if not isinstance(model, str): raise('Не подходящий тип данных.')

        self.__model = model

    def set_task(self, task: str):
        if not isinstance(task, str): raise('Не подходящий тип данных.')

        self.__task = task

    def set_battery(self, battery: int):
        if not isinstance(battery, int): raise('Не подходящий тип данных.')

        self.__battery = battery

    def set_status(self, status: bool):
        if not isinstance(status, bool): raise('Не подходящий тип данных.')

        self.__status = status

    def __str__(self):
        return (f'Серийный номер: {self.__serial_num}\n'
                f'Модель: {self.__model}\n'
                f'Задача: {self.__task}\n'
                f'Батарея: {self.__battery}\n'
                f'Состояние: {self.__status}')

class Athlete:

    def __init__(self, name: str, age: int, sport: str, achievements: list, status: bool):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__achievements = achievements
        self.__status = status

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sport(self):
        return self.__sport

    def get_achievements(self):
        return self.__achievements

    def get_status(self):
        return self.__status

    def set_name(self, name: str):
        if not isinstance(name, str): raise('Не подходящий тип данных.')

        self.__name = name

    def set_age(self, age: int):
        if not isinstance(age, int): raise('Не подходящий тип данных.')

        self.__age = age

    def set_sport(self, sport: str):
        if not isinstance(sport, str): raise('Не подходящий тип данных.')

        self.__sport = sport

    def set_status(self, status: bool):
        if not isinstance(status, bool): raise('Не подходящий тип данных.')

        self.__status = status

    def add_achievement(self, achievement: Achievement):
        if not isinstance(achievement, Achievement): raise('Не подходящий тип данных.')

        self.__achievements.append(achievement)

    def remove_achievement(self, achievement: Achievement):
        if not isinstance(achievement, Achievement): raise('Не подходящий тип данных.')

        for i in range(0, len(self.__achievements), 1):
            if self.__achievements[i] == achievement:
                del self.__achievements[i]
                break

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Возраст: {self.__age}\n'
                f'Вид спорта: {self.__sport}\n'
                f'Достижения: {self.__achievements}\n'
                f'Статус: {self.__status}')

class Achievement:

    def __init__(self):
        pass

