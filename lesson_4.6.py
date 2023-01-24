'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
начиная с указанного,
б) бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
'''

from itertools import count, cycle

# А)

start = int(input("Введите начало:\n"))
end = int(input("Введите конец:\n"))

for i in count(start):
    if i > end:
        break
    else:
        print(i)

# Б)
tmp1 = [2, 2, 10, 7, 4, 11]

iterator = cycle(tmp1)
end = int(input("Введите количество повторений:\n"))
с = 0
for el in cycle(tmp1):
    if с > 10:
        break
    print(el)
    с += 1