'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''

with open("sal.txt", encoding='utf-8') as my_file:
    middle_salary = 0
    a = my_file.readlines()
    for line in a:
        s_name, salary = line.split()
        salary = int(salary)
        middle_salary += salary
        if salary < 20000:
            print(f"\tОклад меньше 25000 руб. у {s_name}-а: {salary} руб.")
    if len(a) > 0:
        middle_salary /= len(a)
        print(f"\tСредняя зарплата: {middle_salary}\n")
