"""
5. Создать (программно) текстовый файл, записать в него
программно набор чисел,разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('text_5.txt', 'w') as my_file:
    my_file.write(input('Введите числа, разделенные пробелами: '))
with open('text_5.txt') as update_file:
    for i in update_file:
        a = i.split()

        print(sum(map(int, a)))
