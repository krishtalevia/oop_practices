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
        if not isinstance(house, str): raise ('Не подходящий тип данных.')

        self.__house = house

    def set_magic_level(self, magic_level: int):
        if not isinstance(magic_level, int): raise ('Не подходящий тип данных.')

        if magic_level > 0:
            self.__magic_level = magic_level

    def set_status(self, status: str):
        if not isinstance(status, str): raise ('Не подходящий тип данных.')

        self.__status = status

    def add_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise('Не подходящий тип данных.')

        self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise ('Не подходящий тип данных.')

        for i in range(0, len(self.__spells), 1):
            if self.__spells[i] == spell:
                del self.__spells[i]
                break

    def increase_magic_level(self, amount: int):
        if not isinstance(amount, int): raise ('Не подходящий тип данных.')

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