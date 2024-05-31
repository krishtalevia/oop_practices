from __future__ import annotations
import random

# 1
class HogwartsStudent:

    def __init__(self, name: str, faculty: str, mana: int, spells: list[Spell]):
        self.__name = name
        self.__faculty = faculty
        self.__mana = mana
        self.__spells = spells

    def get_name(self):
        return self.__name

    def get_faculty(self):
        return self.__faculty

    def get_mana(self):
        return self.__mana

    def get_spells(self):
        spells = ''
        for i in self.__spells:
            i = i.get_name()
            spells += f' {str(i)} |'
        return spells

    def set_name(self, name: str):
        if not isinstance(name, str): raise TypeError('Неподходящий тип данных!')

        self.__name = name

    def set_faculty(self, faculty: str):
        if not isinstance(faculty, str): raise TypeError('Неподходящий тип данных!')

        self.__faculty = faculty

    def set_mana(self, mana: int):
        if not isinstance(mana, int): raise TypeError('Неподходящий тип данных!')

        self.__mana = mana

    def learn_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise TypeError('Неподходящий тип данных!')

        self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__spells), 1):
            if self.__spells[i] == spell:
                del self.__spells[i]
                break

    def cast_spell(self, target: HogwartsStudent):
        if not isinstance(target, HogwartsStudent): raise TypeError('Неподходящий тип данных!')

        current_spell = random.choice(self.__spells)
        self.__mana -= current_spell.get_mana_cost()

        current_spell.cast(target)
        print(f'Осталось маны: {self.__mana}')

    def __str__(self):
        return (f'Имя: {self.__name}\n'
                f'Факультет: {self.__faculty}\n'
                f'Заклинания: {self.get_spells()}\n')

class Spell:

    def __init__(self, name: str, description: str, mana_cost: int):
        self.__name = name
        self.__description = description
        self.__mana_cost = mana_cost

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_mana_cost(self):
        return self.__mana_cost

    def set_name(self, name: str):
        if not isinstance(name, str): raise TypeError('Неподходящий тип данных!')

        self.__name = name

    def set_description(self, description: str):
        if not isinstance(description, str): raise TypeError('Неподходящий тип данных!')

        self.__description = description

    def set_mana_cost(self, mana_cost: int):
        if not isinstance(mana_cost, int): raise TypeError('Неподходящий тип данных!')

        self.__mana_cost = mana_cost

    def cast(self, target: HogwartsStudent):
        if not isinstance(target, HogwartsStudent): raise TypeError('Неподходящий тип данных!')

        target_name = target.get_name()

        print(f'Во время боя с {target_name}, применяется заклинание {self.__name}.\n'
                f'Эффект: {self.__description}\n'
                f'Маны затрачено: {self.__mana_cost}')

    def __str__(self):
        return (f'Название: {self.__name}\n'
                f'Описание: {self.__description}\n'
                f'Стоимость (мана): {self.__mana_cost}\n')

class Hogwarts:

    def __init__(self, students: list[Hogwarts], spells: list[Spell]):
        self.__students = students
        self.__spells = spells

    def get_students(self):
        students = ''
        for i in self.__students:
            i = i.get_name()
            students += f' {str(i)} |'
        return students

    def get_spells(self):
        spells = ''
        for i in self.__spells:
            i = i.get_name()
            spells += f' {str(i)} |'
        return spells

    def enroll_student(self, student: HogwartsStudent):
        if not isinstance(student, HogwartsStudent): raise TypeError('Неподходящий тип данных!')

        self.__students.append(student)

    def teach_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise TypeError('Неподходящий тип данных!')

        self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        if not isinstance(spell, Spell): raise TypeError('Неподходящий тип данных!')

        for i in range(0, len(self.__spells), 1):
            if self.__spells[i] == spell:
                del self.__spells[i]
                break

    def simulate_duel(self, student1: HogwartsStudent, student2: HogwartsStudent):
        if (not isinstance(student1, HogwartsStudent)
                or not isinstance(student2, HogwartsStudent)): raise TypeError('Неподходящий тип данных!')

        while True:
            print(f'----------Атакует студент {student1.get_name()}----------')
            student1.cast_spell(student2)
            if student1.get_mana() <= 0:
                winner = student2.get_name()
                break

            print(f'----------Атакует студент {student2.get_name()}----------')
            student2.cast_spell(student1)
            if student2.get_mana() <= 0:
                winner = student1.get_name()
                break

        print(f'Победил студент {winner}!')
        student1.set_mana(100)
        student2.set_mana(100)

class Program:

    @staticmethod
    def main():

        expelliarmus = Spell('Expelliarmus', 'Обезоруживание', 10)
        stupefy = Spell('Stupefy', 'Оглушение', 20)
        avada_kedavra = Spell('Avada Kedavra', 'Смертельное ранение', 30)
        protego = Spell('Protego', 'Защитный щит', 10)
        petrificus_totalus = Spell('Petrificus Totalus', 'Полная парализация', 20)
        lumos = Spell('Полная парализация', 'Создание источника света', 10)
        expecto_patronum = Spell('Expecto Patronum', 'Призывание патронуса', 30)

        oleg = HogwartsStudent('Олег', 'Слизерин', 100,
                                           [expelliarmus, stupefy, avada_kedavra])
        igor = HogwartsStudent('Игорь', 'Когтевран', 100,
                               [lumos, petrificus_totalus, expecto_patronum])

        hogwarts = Hogwarts([oleg, igor], [expelliarmus, stupefy, avada_kedavra, protego,
                                           petrificus_totalus, lumos, expecto_patronum])

        hogwarts.simulate_duel(oleg, igor)

Program.main()