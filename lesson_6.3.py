'''3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность),
income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}; создать класс Position (должность)
на базе класса Worker; в классе Position реализовать методы
получения полного имени сотрудника (get_full_name) и дохода
с учётом премии (get_total_income); проверить работу примера на
реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Ivan', 'Ivanov', 'Python developer', 200000, 50000)
print(f'Полное имя сотрудника : {p.get_full_name()},позиция: {p.position}')
print(f'Суммарный доход: {p.get_full_salary()}')
