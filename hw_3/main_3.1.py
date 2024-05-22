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
        self.__house = house

    def set_magic_level(self, magic_level: int):
        self.__magic_level = magic_level

    def set_status(self, status: str):
        self.__status = status

