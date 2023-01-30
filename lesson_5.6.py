'''
6. Сформировать (не программно) текстовый файл. В нём каждая
строка должна описывать учебныйпредмет и наличие лекционных,
практических и лабораторных занятий по предмету.Сюда должно
входить и количество занятий. Необязательно, чтобы для
каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

with open("text_6.txt", encoding='utf-8') as my_file:
    res_dict = {}
    a = my_file.readlines()
    for line in a:
        if len(line):
            my_line = line.split()
            hours_sum = 0
            for hours in my_line[1:]:
                if len(hours) > 1:
                    hours_sum += int(hours.split('(')[0])
            res_dict[my_line[0]] = hours_sum
    print(f"\t{res_dict}\n")
