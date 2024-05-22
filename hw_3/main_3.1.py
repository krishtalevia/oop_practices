from __future__ import annotations

# 1.1
class Wizard:

    def __init__(self, name: str, house: str, magic_level: int, spells: list, status: bool):
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
