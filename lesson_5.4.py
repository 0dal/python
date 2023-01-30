'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_4.txt', encoding='UTF-8') as my_file:
    for my_line in my_file:
        for key in translate.keys():
            my_line = my_line.replace(key, translate[key])
    print(my_line)
    with open('text_4new.txt', "a") as my_file2:
        my_file2.write(f"\n{my_line}")
