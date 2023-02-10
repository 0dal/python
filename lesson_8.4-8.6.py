'''
4.
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5.
Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных
о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.

6.
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''


class OfficeTechnics:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_full = [name, price, quantity]
        self.my_store = []

    def storage(self):
        print('\n Сейчас на складе: \n')
        print(', '.join(map(str, self.my_store_full)))
        try:
            new_name = input(f'Введите новое наименование ')
            new_price = int(input(f'Введите цену '))
            new_quantity = int(input(f'Введите количество '))
            new_data = [new_name, new_price, new_quantity]
            self.my_store.append(new_data)
            print(self.my_store)
        except:
            return print(f'Ошибка ввода данных! Данные не внесены.')

        q = input(f'\n Завершить? \n Yes(y) / No(n) ')
        if q == 'Y' or q == 'y':
            self.my_store_full.append(self.my_store)
            print('\n Весь склад: \n')
            print(', '.join(map(str, self.my_store_full)))
        elif q == 'N' or q == 'n':
            return


class Printer(OfficeTechnics):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)


class Scanner(OfficeTechnics):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)


class Xerox(OfficeTechnics):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)


if __name__ == '__main__':
    unit_1 = Printer('hp', 2000, 5)
    unit_2 = Scanner('Canon', 1200, 5)
    unit_3 = Xerox('qqq', 1500, 1)

    OfficeTechnics.storage(unit_1)
    OfficeTechnics.storage(unit_2)
    OfficeTechnics.storage(unit_3)


