from __future__ import annotations

# 1.1
class Wizard:

    def __init__(self, name: str, faculty: str, level: int, spells: list, student_status: bool):
        self.__name = name
        self.__faculty = faculty
        self.__level = level
        if spells == None:
            self.__spells = []
        else:
            self.__spells = spells
        self.__student_status = student_status

