"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = list(input('Введите список элементов через пробел: ').split())

x = 0 # индекс первого элемента

for i in range(len(my_list)):
    if i % 2 == 1:
        my_list[x], my_list[i] = my_list[i], my_list[x]
        x += 2

print(my_list)