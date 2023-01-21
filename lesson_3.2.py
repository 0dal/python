'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''

# 1 вариант
def my_func(name, surname, year, city, email, tel):
    return ''.join([name, surname, year, city, email, tel])
print(my_func( surname = 'Иванов', name = 'Иван', year = '1990', city = 'Москва', email = 'error@mail.ru', tel = '8-916-916-91-69'))


# 2 вариант
def my_func(var_1, var_2, var_3, var_4, var_5, var_6):

    print(f"Имя: {var_1}; "
          f"Фамилия: {var_2}; "
          f"Год рождения: {var_3}, "
          f"Город проживания: {var_4}; "
          f"E-mail: {var_5}; "
          f"Телефон: {var_6}",
          )


name = input('Введите имя пользователя:\n')
surname = input('Введите фамилию пользователя\n')
year_birth = input('Введите год рождения пользователя\n')
city = input('Введите город проживания пользователя\n')
email = input('Введите E-mail пользователя\n')
phone_number = input('Введите телефон пользователя\n')

my_func(var_1=name, var_2=surname, var_3=year_birth, var_4=city, var_5=email, var_6=phone_number)
