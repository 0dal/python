'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
'''
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'сумма двух наибольших аргументов - {my_func(int(input("введите первый аргумент")), int(input("введите второй аргумент")), int(input("введите третий аргумент ")))}')

