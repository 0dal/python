'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_file = open('test.txt', 'w')
my_line = input('Введите текст \n')
while my_line:
    my_file.writelines(my_line)
    line = input('Введите текст \n')
    if not line:
        break

my_file.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_file.close()
