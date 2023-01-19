'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень).
Напишите решения через list и через dict.
'''
s_list = ['winter', 'spring', 'summer', 'autumn']
s_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 2 or month == 12:
    print(s_dict.get(1))
    print(s_list[0])
elif month == 3 or month == 4 or month == 5:
    print(s_dict.get(2))
    print(s_list[1])
elif month == 6 or month == 7 or month == 8:
    print(s_dict.get(3))
    print(s_list[2])

elif month == 9 or month == 10 or month == 11:
    print(s_dict.get(4))
    print(s_list[3])
else:
    print("Такого месяца не существует")
