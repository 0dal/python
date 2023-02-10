"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class ExceptionClass(Exception):

    @staticmethod
    def DivError_func(a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} : Ошибка: На ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {res} \n")


x = ExceptionClass()

x.DivError_func(10, 2)
x.DivError_func(10, 0)
x.DivError_func(-10, 4)
x.DivError_func(0, 10)
