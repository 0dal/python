'''
Создайте собственный класс-исключение, который должен проверять содержимое списка
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''


class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        while True:
            try:
                try:
                    val = int(input('Введите числа по одному: '))
                    a = input(f'Добавляем "{val}" в список. Продолжить? Yes(y)/No(n): ')
                    self.my_list.append(val)
                    if a == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                a = input(f"Это не число! Данные не записаны. Продолжить? Yes(y)/No(n): ")
                if a == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


x = TypeCheck()
x.check_value()
